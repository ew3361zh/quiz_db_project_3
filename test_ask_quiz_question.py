import unittest 
from unittest.mock import patch
from view import view, view_util

class TestAskQuizQuestions(TestCase):

    # TODO connect to test database, clear database

    @patch('view_util.get_user_answer')  # replace the python built in, input method. It's full name is builtins.input
    def test_ask_question(self, mock_get_user_answer):  # note second argument 
        
        # TODO Insert example question(s) into database 
        
        mock_get_user_answer.return_value = 3   # replace with whatever you want your user to answer during this test

        # TODO set up the view, view_model

        view = View()

        # TODO create example question, answer
        view.ask_one_question(question, answer)  # during this method, it will ask for user input, 
        # but the input will be provided by the mock_get_user_answer instead of the real one, so the test won't pause and ask for input 

        # TODO check database to ensure correct result row was added 

  