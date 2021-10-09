import sqlite3
import unittest
from unittest import TestCase

from sql_database import database

from model.quiz_model import QuizQuestion, QuizResult, QuizResultSummary

from exceptions.quiz_error import QuizError


class TestQuizDB(TestCase):

    test_db_url = 'test_questions.db'

    def setUp(self):
        database.db = self.test_db_url

        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('DROP TABLE IF EXISTS quiz_questions')
            conn.execute('DROP TABLE IF EXISTS quiz_results')
        conn.close()

        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute("""CREATE TABLE quiz_questions (
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

        self.db = database.QuizquestionDB()
    

    