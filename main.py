# TODO high level configuration, set up any other modules the program needs

from view import * 

from sql_database.database import QuizquestionDB    # Use this class to use the SQLite DB  

from view.view import View 
from view_model import ViewModel

def main():

    quizquestion_db = QuizquestionDB()
    #vehicle_db = APIVehicleDB()    # Replace the SQLVehicleDB with this to use the API - code will be happy

    quiz_question_view_model = ViewModel(quizquestion_db)

    quiz_question_view = View(quiz_question_view_model)

    topics = quiz_question_view.get_topics()  # do I need to have a place for the topics return to land here?
    
    topic_requested = quiz_question_view.choose_topic(topics)  # so I also am calling the show_topics with topics as argument...
    
    questions, difficulty, points = quiz_question_view.get_questions(topic_requested)

    results = quiz_question_view.ask_questions(questions, difficulty, points)


if __name__ == '__main__':
    main()
