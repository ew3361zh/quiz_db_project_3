import unittest
from unittest import TestCase
from unittest.mock import patch
from view import view, view_util
import builtins
import importlib

class TestAskQuizQuestions(TestCase):

    @patch('view_util.get_user_answer') 
    @patch('builtins.input')

    def test_ask_one_question(self, mock_get_user_answer): # note second argument

        question = 'Is this a fake question?'
        mock_get_user_answer.return_value = 3 # replace with what I want user answer to be for test

        importlib.reload(view)

        mock_view_model = MagicMock()
        mock_view_model.ask_one_question = MagicMock()

        test_view = view.View(mock_view_model)

        start_time = view_util.get_time()
        completed_time = start_time + 5

        # TODO create example question, answer
        # view.ask_one_question('Is this a fake question?', 3) # during this method, it was ask for user input
        # but the input will be provided by the mock_get_user_answer instead of real one so test won't pause to ask for input
        
        

        

        # TODO check database to ensure correct result row was added

if __name__ == '__main__':
    unittest.main()