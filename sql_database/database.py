# TODO talk to SQLite db
# doesn't want to think about how data is presented nor how to talk to UI 
# sends info back to view_model

# abc database would be a model of what any database should have in terms of methods - may leave this for last
# this would allow another type of db to be put in place of the sqlite db (this file)

import sqlite3 
# from .config import db  # .config means import from this directory 
from .config import db_path
from exceptions.quiz_error import QuizError
from model.quiz_model import QuizQuestion, QuizResult, QuizResultSummary
from collections import Counter
db = db_path


class QuizQuestionDB():

    # def create_table():
    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS quiz_questions (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                question_text TEXT NOT NULL, 
                correct_answer TEXT NOT NULL, 
                wrong_answer_1 TEXT NOT NULL,
                wrong_answer_2	TEXT NOT NULL,
                wrong_answer_3	TEXT NOT NULL,
                topic TEXT NOT NULL,
                difficulty INTEGER NOT NULL,
                points INTEGER NOT NULL)"""
            )
            
            conn.execute('''CREATE TABLE IF NOT EXISTS quiz_results (
                user_id TEXT UNIQUE NOT NULL,
                question_id	INTEGER NOT_NULL,
                time_started INTEGER NOT_NULL,
                time_completed INTEGER NOT_NULL,
                question_asked INTEGER NOT_NULL,
                answer_picked INTEGER NOT_NULL,
                is_correct INTEGER NOT_NULL,
                points_available INTEGER NOT_NULL,
                points_earned INTEGER NOT_NULL,
                FOREIGN KEY(question_id) REFERENCES quiz_questions(id))'''
            )
        conn.close()

    def get_topics(self):
        # conn = sqlite3.connect(db)
        with sqlite3.connect(db) as conn:
            results = conn.execute('SELECT topic FROM quiz_questions')
            topics1 = []
            
            for topic in results:
                # if topic in topics:
                #     pass
                # else:
                    topics1.append(topic)
            topics1 = [i[0] for i in topics1]
            topics = {k:topics1.count(k) for k in set(topics1)}
            # print(topics)
            # topics = [i[0] for i in topics]
            
        conn.close()
        # how to get normal string output from tuple sql query (i.e. turn ('x',) into x):
        # https://stackoverflow.com/questions/47716237/python-list-how-to-remove-parenthesis-quotes-and-commas-in-my-list
        # topics = [i[0] for i in topics]
        return topics
    
    def get_questions(self, topic):
        if topic is None:
            raise QuizError('You must select a topic')
        else:
            with sqlite3.connect(db) as conn:
                results = conn.execute('SELECT * FROM quiz_questions WHERE topic = ?', (topic.lower(),))
                questions = [QuizQuestion(*row) for row in results.fetchall()]
            conn.close()
            return questions
        
    
    def add_result(self, result):
        
        if result.answer_picked is None:
            raise QuizError('Question must be answered')
            
        else:
            with sqlite3.connect(db) as conn:
                conn.execute(f'INSERT INTO quiz_results VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                            (result.user_id,
                            result.question_id, 
                            result.time_started, 
                            result.time_completed,
                            result.question_asked, 
                            result.answer_picked,
                            result.is_correct,
                            result.points_available,
                            result.points_earned))
            conn.close()
        
    
    def show_results(self, user_id):
        
        with sqlite3.connect(db) as conn:

            # count of how many questions user was asked
            questions_asked_query = conn.execute('SELECT COUNT(question_id) FROM quiz_results WHERE user_id = ?', (user_id,))
            questions_asked_count = questions_asked_query.fetchone()[0]
            
            # calculation of the difference between sum of time completed and time started for all questions
            time_started_sum_query = conn.execute('SELECT SUM(time_started) FROM quiz_results WHERE user_id = ?', (user_id,))
            time_started_count = time_started_sum_query.fetchone()[0]
            time_completed_sum_query = conn.execute('SELECT SUM(time_completed) FROM quiz_results WHERE user_id = ?', (user_id,))
            time_completed_count = time_completed_sum_query.fetchone()[0]
            total_time_taken = round(time_completed_count - time_started_count, 2)
            # TODO convert time_started_count to readable result for user

            # sum of correct answers
            questions_correct_query = conn.execute('SELECT SUM(is_correct) FROM quiz_results WHERE user_id = ?', (user_id,))
            questions_correct_count = questions_correct_query.fetchone()[0]

            # sum of points available
            points_available_query = conn.execute('SELECT SUM(points_available) FROM quiz_results WHERE user_id = ?', (user_id,))
            points_available_count = points_available_query.fetchone()[0]

            # sum of points_earned
            points_earned_query = conn.execute('SELECT SUM(points_earned) FROM quiz_results WHERE user_id = ?', (user_id,))
            points_earned_count = points_earned_query.fetchone()[0]

            # calculation of % points to 1 decimal place
            percent_correct = round(points_earned_count/points_available_count * 100, 2)


        summary_result = QuizResultSummary(questions_asked_count,
                                        questions_correct_count,
                                        total_time_taken,
                                        points_available_count,
                                        points_earned_count,
                                        percent_correct)             

        conn.close()
        return summary_result
