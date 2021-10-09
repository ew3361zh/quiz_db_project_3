# model class representing one entry for a quiz question and possibly one entry for a quiz result

"""
Model objects 
"""

class QuizQuestion():

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
        return f'{self.id}, {self.question_text}, {self.correct_answer}, {self.wrong_answer_1}, {self.wrong_answer_2}, {self.wrong_answer_3}, {self.topic}, {self.difficulty}, {self.points}'

class QuizResult():

    def __init__(self,
                user_id,
                question_id,
                time_started,
                time_completed,
                question_asked,
                answer_picked,
                is_correct,
                points_available,
                points_earned):
        
        self.user_id = user_id
        self.question_id = question_id
        self.time_started = time_started
        self.time_completed = time_completed
        self.question_asked = question_asked
        self.answer_picked = answer_picked
        self.is_correct = is_correct
        self.points_available = points_available
        self.points_earned = points_earned
    
    def __str__(self):
        return f'{self.user_id}, {self.time_started}, {self.time_completed}, {self.is_correct}, {self.points_available}, {self.points_earned}'


# TODO create QuizResultSummary object

if __name__ == '__main__':
    main()