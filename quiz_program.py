"""
Adaptatation from week5 chainsaws database program
"""
from peewee import *

db = SqliteDatabase('quiz_db.sqlite')

class Quizquestion(Model):
    # id = IntegerField()
    # question_text = CharField()
    # correct_answer = CharField()
    # wrong_answer_1 = CharField()
    # wrong_answer_2 = CharField()
    # wrong_answer_3 = CharField()
    # topic = CharField()
    # difficulty = IntegerField() # TODO add restriction must be between 1-5
    # points = IntegerField() # TODO add restriction must be between 1-100

    class Meta:
        database = db
    
    def __str__(self):
        return f'{self.id}, {self.question_text}: {self.correct_answer}, {self.topic}, {self.difficulty}, {self.points}'


def main():

    menu_text = """
    1. Start New Quiz
    2. View Last Quiz Results
    3. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            start_new_quiz()
        # elif choice == '2':
        #     view_last_quiz_result()
        elif choice == '3':
            break
        else:
            print('Not a valid selection, please try again')

def start_new_quiz():
    db.connect()
    # TODO create function for getting quiz questions
    for q in Quizquestion.select():
        print(q.topic)
    # TODO create function for showing answers in particular format
    # TODO allow user to select from choices using while loop to make sure they're selecting a choice


# def add_new_record():
#     add_name = input('What is the chainsawist\'s name? ')
#     name_from_db_check = Chainsawists.get_or_none(name=add_name) 
#     if name_from_db_check:
#         print('Sorry, that person is already in the database')
#         return
#     else:
#         add_country = input('From which country is the chainsawist? ')
#         add_catches = input('How many catches did they have? ')
#     add_entry = Chainsawists(name=add_name, country=add_country, catches=add_catches)
#     add_entry.save()

# def edit_existing_record():
#     display_all_records()
#     edit_record_id = int(input('What is the number of the record you want to edit? '))
#     id_from_db_check = Chainsawists.get_or_none(id=edit_record_id)
#     if not id_from_db_check:
#         print('Sorry, there\'s no record that matches that number')
#         return
#     else:
#         edit_catches = int(input('What is the new number of catches? '))
#         Chainsawists.update(catches = edit_catches).where(Chainsawists.id == edit_record_id).execute()

# def delete_record():
#     print('todo delete existing record. What if user wants to delete record that does not exist?') 
#     display_all_records()
#     delete_record_id = int(input('What is the number of the record you want to delete? '))
#     id_from_db_check = Chainsawists.get_or_none(id=delete_record_id)
#     if not id_from_db_check:
#         print('Sorry, there\'s no record that matches that number')
#         return
#     else:
#         Chainsawists.delete().where(Chainsawists.id == delete_record_id).execute()


if __name__ == '__main__':
    main()