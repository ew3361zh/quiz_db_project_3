import unittest
from unittest import TestCase
from unittest.mock import patch
from view import view, view_util

class TestAskQuizQuestions(TestCase):

    # TODO connect to test db, clear db

    @patch('view_util.get_user_answer') 
    # replace the python builtin input method with builtins.input

    def test_ask_question(self, mock_get_user_answer): # note second argument

        # TODO inser example questions into db

        mock_get_user_answer.return_value = 3 # replace with what I want user answer to be for test


        # TODO set up view, view_model

        view = View()

        # TODO create example question, answer
        view.ask_one_question(question, answer) # during this method, it was ask for user input
        # but the input will be provided by the mock_get_user_answer instead of real one so test won't pause to ask for input

        # TODO check database to ensure correct result row was added