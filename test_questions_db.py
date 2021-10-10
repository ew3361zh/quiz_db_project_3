import sqlite3
import unittest
from unittest import TestCase

from sql_database import database

from model.quiz_model import QuizQuestion, QuizResult, QuizResultSummary

from exceptions.quiz_error import QuizError


class TestQuizDB(TestCase):

    test_db_url = 'test_questions.sqlite'

    def setUp(self):
        database.db = self.test_db_url

        # not deleting the table first because I don't have methods set up
        # to repopulate new questions into the database - 
        # adding questions isn't part of the program by design
        # but I believe we still need this method to designate the test table?

        with sqlite3.connect(self.test_db_url) as conn:
            # not dropping quiz_questions table because data insert not being executed in this program
            conn.execute('DROP TABLE IF EXISTS quiz_results')
        conn.close()

        with sqlite3.connect(self.test_db_url) as conn:
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

            conn.execute('''CREATE TABLE quiz_results (
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

        self.db = database.QuizQuestionDB()

    def test_get_topics(self):
        # try getting topics as expected
        with sqlite3.connect(self.test_db_url) as conn:
            results = conn.execute('SELECT topic FROM quiz_questions')
            topics = [] 
            for topic in results:
                if topic in topics:
                    pass
                else:
                    topics.append(topic)
        conn.close()
        topics = [i[0] for i in topics]
        self.assertEqual(['space', 'art', 'geoint'], topics)
    
    def test_get_questions_for_topic_doesnt_exist(self):
        # try to get questions if user selects topic not in list (and this somehow gets by)
        topic = 'language' # not an available topic
        with sqlite3.connect(self.test_db_url) as conn:
            results = conn.execute('SELECT * FROM quiz_questions WHERE topic = ?', (topic.lower(),))
            questions = [QuizQuestion(*row) for row in results.fetchall()]
        conn.close()
        self.assertEqual(questions, [])
    
    def test_add_result_correctly(self):
        # test that correctly assembled result object adds to quiz_results db
        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute(f'INSERT INTO quiz_results VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                        (12345,
                        5, 
                        250000000, 
                        250000030,
                        'why though?', 
                        'because I said so',
                        1,
                        100,
                        100))
        conn.close()
        expected = (12345, 5, 250000000, 250000030, 'why though?', 'because I said so', 1, 100, 100)
        print(len(expected))
        self.compare_results_table_to_expected(expected)
    
    # TODO test insert null value for all the fields in the quiz_results table
    # TODO test foreign key for question in quiz_results matches question id in quiz_questions
    # TODO test show results somehow
    
    def compare_results_table_to_expected(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        all_data = conn.execute('SELECT * FROM quiz_results').fetchall()[0]

        # Same rows in DB as entries in expected dictionary
        self.assertEqual(len(expected), len(all_data))

        conn.close()
    
if __name__ == '__main__':
    unittest.main()