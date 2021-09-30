"""
Adaptatation from week5 chainsaws database program
"""
import sqlite3

db = 'questions.sqlite'

def create_table():
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
    conn.close()



# def insert_test_results():
#     # TODO insert test result for question to results db
#     with sqlite3.connect(db) as conn:
#         conn.execute('INSERT INTO products values (1000, "hat")')
#         conn.execute('INSERT INTO products values (1001, "jacket")')
#     conn.close()

def display_all_data():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM quiz_questions WHERE rowid = 1')
    print(f'Question 1: ')
    for row in results:
        print(row) # each row is a tuple

    conn.close()

create_table()
display_all_data()
# def display_one_product(product_name):
#     conn = sqlite3.connect(db)
#     results = conn.execute('SELECT * FROM products WHERE name like ?', (product_name,))
#     first_row = results.fetchone()
#     if first_row:
#         print('Your product is:', first_row) # upgrade to row factory later
#     else:
#         print('not found')
#     conn.close()

# def create_new_product():
#     new_id = int(input('enter new id: '))
#     new_name = input('enter new name: ')
    
#     with sqlite3.connect(db) as conn:
#     # don't use format strings for commit SQL statements
#     # conn.execute(f'INSERT INTO products VALUES({new_id}, "{new_name}")') # wrong - will make program crash if unacceptable character entered as variable
#         conn.execute(f'INSERT INTO products VALUES(?, ?)', (new_id, new_name)) # right - using parameterized queries
#     conn.close()

# def update_product():
#     updated_product = 'wool hat'
#     update_id = 1000

#     with sqlite3.connect(db) as conn:
#         conn.execute('UPDATE products SET name = ? WHERE id = ?', (updated_product, update_id))
#     conn.close()