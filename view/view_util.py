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
    print('\n')
    while topic_requested.isnumeric() is False or int(topic_requested) > len(topics) or int(topic_requested) == 0: # validation based on keys and using .lower() to make sure case isn't a cause of user input being rejected
        print('Please only choose from one of the below listed categories\n')
        # for count, topic in enumerate(topics):
        #     print(count+1, topic)
        count = 1
        for topic, topic_count in topics.items():
            print(f'{count}: {topic} ({topic_count} questions)')
            count = count + 1
        print('\n')
        topic_requested = input('Try again and please select from the topics by number: ')
        print('\n')
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
    function prints current time (start of quiz time) and returns it as a timestamp for tracking how much time user spent on question
    """
    current_time = datetime.now().timestamp()
    header(f'Quiz is starting at {datetime.fromtimestamp(round(current_time))}')
    return current_time

def show_randomized_answers(question):
    """ 
    function to take list of answers for a particular quiz question and print them in a random order
    """
    answers = [question.correct_answer, question.wrong_answer_1, question.wrong_answer_2, question.wrong_answer_3]
    random.shuffle(answers)
    for q_num, a in enumerate(answers):
        print(f'{q_num+1}:{a}')
    return answers

def get_user_answer():
    """ 
    function to validate user response is within range of possible answers
    """
    user_answer = input('What is your answer? ')
    while user_answer.isnumeric() is False or int(user_answer) not in range(1,5):
        print('\n')
        user_answer = input('Please try again and select the number answer you believe is correct: ')
    user_answer = int(user_answer)-1
    print('\n')
    return user_answer

def check_if_correct(user_guess, correct_answer):
    """ 
    function to check user answer against correct answer
    """
    if user_guess == correct_answer:
        print('Correctamundo!')
        return True
    else:
        print(f'I\'m deeply sorry but the correct answer is {correct_answer}')
        return False