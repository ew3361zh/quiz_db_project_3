# doesn't want to think about details of how to query db, delegate that to view_model

import random

from view.view_util import input_pos_int, header, validate_topic_chosen, generate_user_id, get_time, show_randomized_answers, get_user_answer, check_if_correct
from model.quiz_model import QuizQuestion, QuizResult, QuizResultSummary
from exceptions.quiz_error import QuizError

class View:

    def __init__(self, view_model):
        self.view_model = view_model


    def start_quiz(self):
        user_id = generate_user_id()
        topics = self.get_topics()
        topic_requested = self.choose_topic(topics)
        questions = self.get_questions(topic_requested)
        self.ask_questions(questions, user_id)
        self.show_results(user_id)

    def get_topics(self):

        header('Welcome to our quiz program!\nYou can choose to answer questions from the following categories:')

        try:           
            topics = self.view_model.get_topics()
            return topics
        except QuizError as e:
            print(str(e))

    def choose_topic(self, topics):

        for count, topic in enumerate(topics):
            print(count+1, topic)
        topic_requested_num = validate_topic_chosen(topics)
        topic_requested = topics[topic_requested_num].upper()
        print(f'You selected {topic_requested.upper()}')
        return topic_requested
    
    def get_questions(self, topic):
        
        try:
            questions = self.view_model.get_questions(topic) # TODO use question object to return questions, not weird lists and dictionaries
            return questions
        except QuizError as e:
            print(str(e))


    def ask_questions(self, questions, user_id):
        question_counter = 0
        for question in questions:
            result = self.ask_one_question(question, user_id, question_counter)
            try:
                self.view_model.add_result(result)
            except QuizError as e:
                print(str(e))
            question_counter = question_counter + 1 # count of which question user is on needs to increase each time a question is asked


    def ask_one_question(self, question, user_id, question_counter):
            
        header(f'Question #{question_counter+1} in the {question.topic} category\nDifficulty of {question.difficulty} with {question.points} points available:')
        print(question.question_text)             
        answers = show_randomized_answers(question)
        time_started = get_time()
        print('\n')
        user_answer = get_user_answer()
        time_completed = get_time()
        print(f'User answer is {answers[user_answer]}')
        is_correct = check_if_correct(answers[user_answer], question.correct_answer)
        if is_correct:
            points_earned = question.points
        else:
            points_earned = 0
        result = QuizResult(user_id, 
                            question.id, 
                            time_started, 
                            time_completed, 
                            question.question_text, 
                            answers[user_answer],
                            is_correct,
                            question.points,
                            points_earned )
        return result

    def show_results(self, user_id):
        
        try:
            summary_result = self.view_model.show_results(user_id)
            header('Here are your quiz results!')
            if summary_result.questions_correct == 1:
                print(f'User got {summary_result.questions_correct} question correct out of a possible {summary_result.questions_asked}')
            else:
                print(f'User got {summary_result.questions_correct} questions correct out of a possible {summary_result.questions_asked}')
            print(f'Total time taken was {summary_result.time_taken} seconds')
            print(f'User earned {summary_result.total_points_earned} out of a possible {summary_result.total_points_available} points which is a score of {summary_result.percent_correct}%')
            print('\n')
            print('Thank you for using the quiz program!')
        except QuizError as e:
            print(str(e))

   