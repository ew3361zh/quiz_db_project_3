"""
Adaptatation from week5 chainsaws database program
"""
import sqlite3
import random
from datetime import datetime, date, time

db = 'questions.sqlite'

class Quizquestion:

    def __init__(self, 
                id, 
                question_text, 
                correct_answer, 
                wrong_answer_1,
                wrong_answer_2,
                wrong_answer_3,
                topic,
                difficulty,
                points):

        self.id = id
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.wrong_answer_1 = wrong_answer_1
        self.wrong_answer_2 = wrong_answer_2
        self.wrong_answer_3 = wrong_answer_3
        self.topic = topic
        self.difficulty = difficulty
        self.points = points 

    
    def __str__(self):
        return f'{self.id}, {self.question_text}: {self.correct_answer}, {self.topic}, {self.difficulty}, {self.points}'
    
def get_topics():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT topic FROM quiz_questions')
    topics = [] 
    for topic in results:
        if topic in topics:
            pass
        else:
            topics.append(topic)
    conn.close()
    # how to get normal string output from tuple sql query (i.e. turn ('x',) into x):
    # https://stackoverflow.com/questions/47716237/python-list-how-to-remove-parenthesis-quotes-and-commas-in-my-list
    topics = [i[0] for i in topics]
    return topics

def get_questions(topic):
    #TODO needs to be sent topic as a parameter to know which questions to query
    conn = sqlite3.connect(db)
    # TODO get results for all matching questions from topic (put into dictionary?)
    results = conn.execute('SELECT * FROM quiz_questions WHERE topic = ?', (topic,))
    questions_answers = []
    for row in results:
        questions_answers.append((row[1], [row[2], row[3], row[4], row[5]]))
    questions_dict = dict(questions_answers)
    # print(questions_dict)
    conn.close()
    # TODO return questions and possible answers together but randomized or randomize 
    # when print them out
    return questions_dict



def create_table():
    # TODO create table if not exists statement for results table
    #context manager - don't need to commit as before
    with sqlite3.connect(db) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS quiz_questions (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            question_text TEXT NOT NULL, 
            correct_answer TEXT NOT NULL, 
            wrong_answer_1 TEXT NOT NULL,
            wrong_answer_2	TEXT NOT NULL,
            wrong_answer_3	TEXT NOT NULL,
            topic TEXT NOT NULL,
            difficulty INTEGER NOT NULL,
            points INTEGER NOT NULL)"""
        )
        # conn.execute("""DROP TABLE quiz_results""")
        conn.execute('''CREATE TABLE IF NOT EXISTS quiz_results (
            question_id	INTEGER,
            time_started INTEGER,
            time_completed INTEGER,
            question_asked INTEGER,
            answer_picked INTEGER,
            is_correct INTEGER,
            points_available INTEGER,
            points_earned INTEGER,
            score_as_percent INTEGER,
            FOREIGN KEY(question_id) REFERENCES quiz_questions(id))'''
        )
    conn.close()

def ask_questions(questions_dict):
    question_count = 0
    for question, answer in questions_dict.items():
        print(f'Question #{question_count+1}:')
        print(question)
        correct_answer = answer[0]
        random.shuffle(answer)
        for q_num, a in enumerate(answer):
            print(f'{q_num+1}:{a}')
        user_answer = input('What is your answer? ')
        while user_answer.isnumeric() is False or int(user_answer) not in range(1,5):
            user_answer = input('Please try again and select the number answer you believe is correct')
        user_answer = int(user_answer)-1
        print(f'User answer is {answer[user_answer]}')
        if answer[user_answer] == correct_answer:
            print('Correctamundo!')
        else:
            print(f'I\'m deeply sorry but the correct answer is {answer[0]}')

# def insert_test_results():
#     # TODO insert test result for question to results db
#     with sqlite3.connect(db) as conn:
#         conn.execute('INSERT INTO products values (1000, "hat")')
#         conn.execute('INSERT INTO products values (1001, "jacket")')
#     conn.close()

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
    total_score = 0
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
    topic_requested = topics[topic_requested_num]
    print(f'You selected {topic_requested.upper()}')
    questions_dict = get_questions(topic_requested)
    ask_questions(questions_dict)
    # total_score = ask_questions(topic_questions, total_score) #processing function called
    # score_output(total_score, len(topic_questions)) #output results to user, send down both updated total score from ask_questions 
    #                                                 #function return and the number of questions in their particular chosen topic area
    print('\n')
    print('Thank you for playing!\n')




if __name__ == '__main__':
    main()