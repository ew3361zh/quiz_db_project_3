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


        # your tests can populate the questions table with example questions 

        with sqlite3.connect(self.test_db_url) as conn:
            # not dropping quiz_questions table because data insert not being executed in this program
            conn.execute('DROP TABLE IF EXISTS quiz_results')
        conn.close()


        # you can also call the method in your code to create the database, then you know it has the same structure 
        # that your code uses. Avoid problems if you need to modify the DB and forget to change this SQL
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

        # This is the same logic as your code.  We want to avoid complex logic in tests. Otherwise we'll have to test the tests.  

        # insert test topics into DB, for example 'trees' and 'cats' and 'space' or whatever 

        # call the get_topics method in database.py, save return value - the test needs to interact with real methods or DB in your code 

        # assert the method returns the example topics 

        # self.assertEqual(['trees', 'cats', 'space'], topics)



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
        self.assertEqual(['space', 'art', 'geoint'], topics)   # this is going to fail if you add more topics 

    
    def test_get_questions_for_topic_doesnt_exist(self):

        # these tests are not calling any functions methods in your code. They are interacting with the test db 
        # that's set up in this file  - so will they tell you anything about how the program code works? 

        # try to get questions if user selects topic not in list (and this somehow gets by)
        topic = 'language' # not an available topic
        with sqlite3.connect(self.test_db_url) as conn:
            results = conn.execute('SELECT * FROM quiz_questions WHERE topic = ?', (topic.lower(),))
            questions = [QuizQuestion(*row) for row in results.fetchall()]
        conn.close()
        self.assertEqual(questions, [])
    
    def test_add_result_correctly(self):
        # test that correctly assembled result object adds to quiz_results db
        result = QuizResult(12345, 5, 250000000, 250000030, 'why though?', 'because I said so', 1, 100, 100)
        with sqlite3.connect(self.test_db_url) as conn:
            self.db.add_result(result)
        conn.close()
        expected = (12345, 5, 250000000, 250000030, 'why though?', 'because I said so', 1, 100, 100)
        self.compare_results_table_to_expected(expected)
    
    def test_insert_null_user_answer_into_quiz_result_entry(self):
        # user only contributes input to two pieces of the db: the topic selected and an answer to a question
        # this tests if a null response somehow gets by the check in place in view_utils
        result_null = QuizResult(12345, 5, 250000000, 250000030, 'why though?', None, 1, 100, 100)
        conn = sqlite3.connect(self.test_db_url)
        with self.assertRaises(QuizError):
            self.db.add_result(result_null)

    def test_user_selects_no_topic_raises_error(self):
        # test to check if error is raised if second of two user inputs is null - their selected topic
        topic_null = None
        conn = sqlite3.connect(self.test_db_url)
        with self.assertRaises(QuizError):
            self.db.get_questions(topic_null)

    def compare_results_table_to_expected(self, expected):
        # test that correctly assembled result object adds to quiz_results db
        with sqlite3.connect(self.test_db_url) as conn:
            all_data = conn.execute('SELECT * FROM quiz_results').fetchall()[0]
            # Same rows in DB as entries in expected dictionary
            self.assertEqual(len(expected), len(all_data))
        conn.close()
            
    
if __name__ == '__main__':
    unittest.main()