"""
Adaptatation from week5 chainsaws database program
"""
from sql_database.database import Quizquestion
import sqlite3
import random
from datetime import datetime, date, time
import uuid

# db = 'questions.sqlite'
    
# def get_topics():
    

# def get_questions(topic):
    
    
    # print(questions_dict)
    
    # TODO return questions and possible answers together but randomized or randomize 
    # when print them out

def ask_questions(topic_requested, questions_dict, difficulty, points):
    time_started = datetime.now()
    user_id = str(uuid.uuid4())
    question_counter = 0
    for question, answer in questions_dict.items():
        time_started = datetime.now()
        print('\n')
        print(f'Question #{question_counter+1} in the {topic_requested} category')
        print(f'Difficulty of {difficulty[question_counter]} with {points[question_counter]} points available:')
        print('\n')
        print(question)
        print('\n')
        correct_answer = answer[0]
        random.shuffle(answer)
        for q_num, a in enumerate(answer):
            print(f'{q_num+1}:{a}')
        print('\n')
        user_answer = input('What is your answer? ')
        while user_answer.isnumeric() is False or int(user_answer) not in range(1,5):
            print('\n')
            user_answer = input('Please try again and select the number answer you believe is correct')
        time_completed = datetime.now()
        user_answer = int(user_answer)-1
        print('\n')
        print(f'User answer is {answer[user_answer]}')
        print('\n')
        is_correct = 1
        if answer[user_answer] == correct_answer:
            print('Correctamundo!')
        else:
            print(f'I\'m deeply sorry but the correct answer is {correct_answer}')
            is_correct = 0
        if is_correct == 1:
            points_earned = points[question_counter]
        else:
            points_earned = 0
        with sqlite3.connect(db) as conn:
            conn.execute(f'INSERT INTO quiz_results VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                        (user_id,
                        question_counter+1, 
                        time_started, 
                        time_completed,
                        question, 
                        answer[user_answer],
                        is_correct,
                        points[question_counter],
                        points_earned))
        conn.close()
        question_counter = question_counter + 1
    return user_id

def show_results(user_id):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM quiz_results WHERE user_id = ?', (user_id,))
    most_recent_quiz_results = []
    # for row in results:
    #     #TODO query database to get results and display them to user
    # conn.close()


def validate_topic_choice(topics):
    topic_requested = input('Please select the number of the topic would you like to be quizzed: ')
    print('\n')
    while topic_requested.isnumeric() is False or int(topic_requested) > len(topics) or int(topic_requested) == 0: #validation based on keys and using .lower() to make sure case isn't a cause of user input being rejected
        print('Please only choose from one of the below listed categories\n')
        for count, topic in enumerate(topics):
            print(count+1, topic)
        print('\n')
        topic_requested = input('Try again and please select from the topics by number: ')
    topic_requested = int(topic_requested)-1
    return topic_requested #return chosen q/a sub dictionary to main for use in the ask_questions function

def main():
    create_table()
    print('\n')
    print('Welcome to our quiz program!\n')
    print('You can choose to answer questions from the following categories:\n')
    # TODO method to query db to get list of topics and return list without duplicates
    topics = get_topics()
    for count, topic in enumerate(topics):
        print(count+1, topic)
    print('\n')
    topic_requested_num = validate_topic_choice(topics)
    topic_requested = topics[topic_requested_num].upper()
    print(f'You selected {topic_requested}')
    questions_dict, difficulty, points = get_questions(topic_requested)
    user_id = ask_questions(topic_requested, questions_dict, difficulty, points)
    show_results(user_id)
    print('\n')
    print('Thank you for playing!\n')




if __name__ == '__main__':
    main()