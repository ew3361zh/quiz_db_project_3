# TODO high level configuration, set up any other modules the program needs

from view import * 

from sql_database.database import QuizQuestionDB    # Use this class to use the SQLite DB  

from view.view import View 
from view_model import ViewModel

def main():

    quizquestion_db = QuizQuestionDB()

    quiz_question_view_model = ViewModel(quizquestion_db)

    quiz_question_view = View(quiz_question_view_model)

    quiz_question_view.start_quiz()  # starts quiz in view
    

if __name__ == '__main__':
    main()
