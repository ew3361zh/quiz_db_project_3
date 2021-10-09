# TODO user-interaction: getting data, printing data; details delegated to view_utils
# doesn't want to think about details of how to query db, delegate that to view_model

import random

from view.view_util import input_pos_int, header, validate_topic_chosen, generate_user_id, get_time, ask_one_question
from model.quiz_model import QuizQuestion, QuizResult
from exceptions.quiz_error import QuizError

class View:

    def __init__(self, view_model):
        self.view_model = view_model


    def start_quiz(self):
        user_id = generate_user_id() #TODO make view_util for getting user_id
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


    # TODO redesign ask_questions around question object
    # TODO make ask_question a view_util
    # TODO don't forget to add user_id as parameter or if results are being recorded in another piece put it there
    def ask_questions(self, questions, user_id):
        
        for question_counter in range(len(questions)):
            result = ask_one_question(questions, question_counter, user_id)
            
        # for question, answer in questions.items():
                      
            # correct_answer = answer[0]
            # random.shuffle(answer)
            # for q_num, a in enumerate(answer):
            #     print(f'{q_num+1}:{a}')
            # print('\n')
            # user_answer = input('What is your answer? ')
            # while user_answer.isnumeric() is False or int(user_answer) not in range(1,5): # TODO add to view_util?
            #     print('\n')
            #     user_answer = input('Please try again and select the number answer you believe is correct')
            # # time_completed = get_time()
            # user_answer = int(user_answer)-1
            # print('\n')
            # print(f'User answer is {answer[user_answer]}')
            # print('\n')
            # is_correct = 1
            # if answer[user_answer] == correct_answer: # TODO add as view_util?
            #     print('Correctamundo!')
            # else:
            #     print(f'I\'m deeply sorry but the correct answer is {correct_answer}')
            #     is_correct = 0
            # if is_correct == 1: # TODO add to view_util?
            #     points_earned = points[question_counter]
            # else:
            #     points_earned = 0
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
            question_counter = question_counter + 1 # count of which question user is on needs to increase each time a question is asked
        self.show_results(user_id)
    

    def show_results(self, user_id):
        
        try:
            results = self.view_model.show_results(user_id)
            # for result in results: # TODO use print out from database as model for here but after it's been changed to a Result Summary object
            #     print(result)
            # print('\n')
            # print('Thank you for using the quiz program! ')
        except QuizError as e:
            print(str(e))

   