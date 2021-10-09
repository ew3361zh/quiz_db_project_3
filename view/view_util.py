"""
Input and validation utilities
"""

import uuid
from datetime import datetime, date, time

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

# TODO 1. maybe a randomize and print q answers function? or separate into two functions - a randomize and a display?
# TODO 2. see view ask_questions function for more possible view_util additions