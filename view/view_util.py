#TODO write input validations, is there data entered, is this a number (and in the range I want it to be)
"""
Input and validation utilities
"""

def input_pos_int(question):
    while True:
        try:
            number = int(input(question))
            if number < 1:
                print('Enter a positive number: ')
            else:
                return number
        except ValueError:
            print('Please enter a number: ')

# TODO necessary to have header util function?
def header(text):
    stars = len(text) * '*'
    print(f'\n{stars}\n{text}\n{stars}\n')

def validate_topic_chosen(topics):
    topic_requested = input('Please select the number of the topic would you like to be quizzed: ')
    while topic_requested.isnumeric() is False or int(topic_requested) > len(topics) or int(topic_requested) == 0: #validation based on keys and using .lower() to make sure case isn't a cause of user input being rejected
        print('Please only choose from one of the below listed categories\n')
        for count, topic in enumerate(topics):
            print(count+1, topic)
        print('\n')
        topic_requested = input('Try again and please select from the topics by number: ')
    topic_requested = int(topic_requested)-1
    return topic_requested
# TODO:
# 1. maybe a randomize and print q answers function? or separate into two functions - a randomize and a display?
# 2. 