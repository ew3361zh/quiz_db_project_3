"""
Input and validation utilities
"""

import random
import uuid
from datetime import datetime, date, time
from model.quiz_model import QuizResult

def input_pos_int(question):
    """
    function to ensure positive integer input from user
    """
    while True:
        try:
            number = int(input(question))
            if number < 1:
                print('Enter a positive number: ')
            else:
                return number
        except ValueError:
            print('Please enter a number: ')

def header(text):
    """
    function to add some pizzazz to printing out things to user in terminal
    """
    stars = len(text) * '*'
    print(f'\n{stars}\n{text}\n{stars}\n')

def validate_topic_chosen(topics):
    """ 
    function to validate topic from user
    """
    print('\n')
    topic_requested = input('Please select the number of the topic would you like to be quizzed: ')
    while topic_requested.isnumeric() is False or int(topic_requested) > len(topics) or int(topic_requested) == 0: # validation based on keys and using .lower() to make sure case isn't a cause of user input being rejected
        print('Please only choose from one of the below listed categories\n')
        for count, topic in enumerate(topics):
            print(count+1, topic)
        print('\n')
        topic_requested = input('Try again and please select from the topics by number: ')
    topic_requested = int(topic_requested)-1
    return topic_requested

def generate_user_id():
    """ 
    function to generate a unique user ID
    """
    user_id = str(uuid.uuid4())
    return user_id

def get_time():
    """
    function gets current time and turns it into a timestamp for tracking how much time user spent on question
    """
    current_time = datetime.now().timestamp()
    return current_time

def ask_one_question(questions, question_counter, user_id):
    for question in questions:
        if questions.id == question_counter:
            header(f'Question #{question_counter+1} in the {question.topic} category\nDifficulty of {question.difficulty} with {question.points} points available:')
            print(questions.question)
            answers = show_randomized_answers(question)
            time_started = get_time()
            print('\n')
            user_answer = get_user_answer()
            print(f'User answer is {answers[user_answer]}')
            is_correct = check_if_correct(answers[user_answer], question.correct_answer)
        else:
            pass

def show_randomized_answers(question):
    answers = [question.correct_answer, question.wrong_answer_1, question.wrong_answer_2, question.wrong_answer_3]
    random.shuffle(answers)
    for q_num, a in enumerate(answers):
        print(f'{q_num+1}:{a}')
    return answers

def get_user_answer():
    user_answer = input('What is your answer? ')
    while user_answer.isnumeric() is False or int(user_answer) not in range(1,5):
        print('\n')
        user_answer = input('Please try again and select the number answer you believe is correct')
    user_answer = int(user_answer)-1
    print('\n')
    return user_answer

def check_if_correct(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False

# TODO 2. see view ask_questions function for more possible view_util additions