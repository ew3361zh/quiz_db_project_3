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

        # with sqlite3.connect(self.test_db_url) as conn:
        #     conn.execute('DROP TABLE IF EXISTS quiz_questions')
        #     conn.execute('DROP TABLE IF EXISTS quiz_results')
        # conn.close()

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
    
    
    
    # def compare_db_to_expected(self, expected):

    #     conn = sqlite3.connect(self.test_db_url)
    #     all_data = conn.execute('SELECT * FROM quiz_question').fetchall()

    #     # Same rows in DB as entries in expected dictionary
    #     self.assertEqual(len(expected.keys()), len(all_data))

    #     for row in all_data:
    #         # Vehicle exists, and mileage is correct
    #         self.assertIn(row[0], expected.keys())
    #         self.assertEqual(expected[row[0]], row[1])

    #     conn.close()
    
if __name__ == '__main__':
    unittest.main()