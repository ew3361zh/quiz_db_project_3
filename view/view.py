# TODO user-interaction: getting data, printing data; details delegated to view_utils
# doesn't want to think about details of how to query db, delegate that to view_model

import random
from datetime import datetime, date, time
import uuid
from view.view_util import input_pos_int, header, validate_topic_chosen
from model.quiz_model import Quizquestion
from exceptions.quiz_error import QuizError

class View:

    def __init__(self, view_model):
        self.view_model = view_model

    # main calls this function first which basically kicks off everything and nothing goes back to main right now
    # TODO send topics to choose topics vs return topics to main which wasn't working?
    def get_topics(self):

        header('Welcome to our quiz program!\nYou can choose to answer questions from the following categories:')

        try:           
            topics = self.view_model.get_topics()
            self.choose_topic(topics)
        except QuizError as e:
            print(str(e))

    def choose_topic(self, topics):

        for count, topic in enumerate(topics):
            print(count+1, topic)
        topic_requested_num = validate_topic_chosen(topics)
        topic_requested = topics[topic_requested_num].upper()
        print(f'You selected {topic_requested.upper()}')
        self.get_questions(topic_requested)

    
    def get_questions(self, topic):
        
        try:
            questions, difficulty, points = self.view_model.get_questions(topic)
            self.ask_questions(questions, difficulty, points, topic)
        except QuizError as e:
            print(str(e))


    def ask_questions(self, questions, difficulty, points, topic_requested):
        
        time_started = datetime.now()
        user_id = str(uuid.uuid4())
        question_counter = 0
        for question, answer in questions.items():
            time_started = datetime.now()
            header(f'Question #{question_counter+1} in the {topic_requested} category\nDifficulty of {difficulty[question_counter]} with {points[question_counter]} points available:')
            print(question)
            print('\n')
            correct_answer = answer[0]
            random.shuffle(answer)
            for q_num, a in enumerate(answer):
                print(f'{q_num+1}:{a}')
            print('\n')
            user_answer = input('What is your answer? ')
            while user_answer.isnumeric() is False or int(user_answer) not in range(1,5): # TODO add to view_util?
                print('\n')
                user_answer = input('Please try again and select the number answer you believe is correct')
            time_completed = datetime.now()
            user_answer = int(user_answer)-1
            print('\n')
            print(f'User answer is {answer[user_answer]}')
            print('\n')
            is_correct = 1
            if answer[user_answer] == correct_answer: # TODO add as view_util?
                print('Correctamundo!')
            else:
                print(f'I\'m deeply sorry but the correct answer is {correct_answer}')
                is_correct = 0
            if is_correct == 1: # TODO add to view_util?
                points_earned = points[question_counter]
            else:
                points_earned = 0
            result = [] # TODO have a separate compiler for result? view_util?
            result.append(user_id)
            result.append(question_counter+1)
            result.append(time_started)
            result.append(time_completed)
            result.append(question)
            result.append(answer[user_answer])
            result.append(is_correct)
            result.append(points[question_counter])
            result.append(points_earned)
            try:
                self.view_model.add_result(result)
            except QuizError as e:
                print(str(e))
        self.show_results(user_id)


    def show_results(self, user_id):
        
        try:
            results = self.view_model.show_results(user_id)
            for result in results: # TODO add to view_util to print out results more cleanly
                print(result)
            print('\n')
            print('Thank you for using the quiz program! ')
        except QuizError as e:
            print(str(e))

   