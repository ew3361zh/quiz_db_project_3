#TODO write input validations, is there data entered, is this a number (and in the range I want it to be)
"""
Input and validation utilities
"""

# too nonspecific?
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

# TODO:
# 1. maybe a randomize and print q answers function? or separate into two functions - a randomize and a display?
# 2. 