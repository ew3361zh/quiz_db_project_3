# TODO talk to SQLite db
# doesn't want to think about how data is presented nor how to talk to UI 
# sends info back to view_model

# abc database would be a model of what any database should have in terms of methods - may leave this for last
# this would allow another type of db to be put in place of the sqlite db (this file)

import sqlite3 
# from .config import db  # .config means import from this directory 
from .config import db_path
from exceptions.quiz_error import QuizError

# from database import VehicleDB TODO rewatch videos on abstract methods
from model.quiz_model import Quizquestion
from utils.validation import ensure_positive_int

db = db_path
# from utils.validation import TODO write validation for ints and more specifically for ints within a certain range

class QuizquestionDB():

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
            # conn.execute("""DROP TABLE quiz_results""") # keeping in case I need it
            conn.execute('''CREATE TABLE IF NOT EXISTS quiz_results (
                user_id TEXT,
                question_id	INTEGER,
                time_started INTEGER,
                time_completed INTEGER,
                question_asked INTEGER,
                answer_picked INTEGER,
                is_correct INTEGER,
                points_available INTEGER,
                points_earned INTEGER,
                FOREIGN KEY(question_id) REFERENCES quiz_questions(id))'''
            )
        conn.close()

    def get_topics(self):
        # conn = sqlite3.connect(db)
        with sqlite3.connect(db) as conn:
            results = conn.execute('SELECT topic FROM quiz_questions')
            topics = [] 
            for topic in results:
                if topic in topics:
                    pass
                else:
                    topics.append(topic)
        conn.close()
        # how to get normal string output from tuple sql query (i.e. turn ('x',) into x):
        # https://stackoverflow.com/questions/47716237/python-list-how-to-remove-parenthesis-quotes-and-commas-in-my-list
        topics = [i[0] for i in topics]
        return topics
    
    def get_questions(self, topic):
        # conn = sqlite3.connect(db)
        with sqlite3.connect(db) as conn:
            results = conn.execute('SELECT * FROM quiz_questions WHERE topic = ?', (topic.lower(),))
            questions_answers = []
            difficulty = []
            points = []
            for row in results:
                questions_answers.append((row[1], [row[2], row[3], row[4], row[5]]))
                difficulty.append(row[7]) 
                points.append(row[8])
            questions_dict = dict(questions_answers)
        conn.close()
        return questions_dict, difficulty, points
    
    def add_result(self, result):
        # TODO get all the below data into a result variable as list(?)
        # possibly try Clara's version where she records rows_modified as variable for execute statement
        with sqlite3.connect(db) as conn:
            conn.execute(f'INSERT INTO quiz_results VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                        (result[0],
                        result[1], 
                        result[2], 
                        result[3],
                        result[4], 
                        result[5],
                        result[6],
                        result[7],
                        result[8]))
        conn.close()
    
    def show_results(self, user_id):
        # conn = sqlite3.connect(db)
        with sqlite3.connect(db) as conn:

            # TODO create results_summary object in objects and import here to make more readable
            
            # count of how many questions user was asked
            questions_asked_query = conn.execute('SELECT COUNT(question_id) WHERE used_id = ?', (used_id))
            questions_asked_count = questions_asked_query.fetchone()[0]
            
            # calculation of the difference between sum of time completed and time started for all questions
            time_started_sum_query = conn.execute('SELECT SUM(time_started) WHERE used_id = ?', (used_id))
            time_started_count = time_completed_sum_query.fetchone()[0]
            time_completed_sum_query = conn.execute('SELECT SUM(time_completed) WHERE used_id = ?', (used_id))
            time_completed_count = time_completed_sum_query.fetchone()[0]
            total_time_taken = time_completed_count - time_started_count
            # TODO convert time_started_count to readable result for user

            # sum of correct answers
            questions_correct_query = conn.execute('SELECT SUM(is_correct) WHERE used_id = ?', (used_id))
            questions_correct_count = questions_correct_query.fetchone()[0]

            # sum of points available
            points_available_query = conn.execute('SELECT SUM(points_available) WHERE used_id = ?', (used_id))
            points_available_count = points_available_query.fetchone()[0]

            # sum of points_earned
            points_earned_query = conn.execute('SELECT SUM(points_earned) WHERE used_id = ?', (used_id))
            points_earned_count = points_earned_query.fetchone()[0]

            # calculation of % points to 1 decimal place
            percent_correct = round(points_earned_count/points_available_count * 100, 1)
                                
            print(f'User got {questions_correct_count} questions correct out of a possible {questions_asked_count}')
            print(f'Total time taken was {total_time_taken} units')
            print(f'User earned {points_earned_count} out of a possible {points_available_count} points which is a score of {percent_correct}%')

        conn.close()
        # return results
