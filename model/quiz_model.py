# model class representing one entry for a quiz question and possibly one entry for a quiz result

"""
Model objects 
"""

class Quizquestion():

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
        return f'{self.id}, {self.question_text}, {self.correct_answer}, {self.topic}, {self.difficulty}, {self.points}'

if __name__ == '__main__':
    main()