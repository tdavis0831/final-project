
"""Script to seed database."""

import os
import json

import crud
import model
import server

os.system("dropdb quizzes")
os.system("createdb quizzes")

model.connect_to_db(server.app)
model.db.create_all()


with open("data/screenings.json") as f:
    screenings_data = json.loads(f.read())

# print(screenings_data)
# print(type(screenings_data))

for quiz in screenings_data:
    db_test = crud.create_test(quiz["test_title"])
    
    for question in quiz["questions"]:
        db_question = crud.create_question(question["test_question"])
            
        db_test_question=crud.create_test_question(db_test, db_question)
    
        db_rubric = crud.create_rubric(quiz["test_rubric"], db_test)

    # for test_name in quiz["test_name"]:
    #     db_test = crud.create_test(list(test_name.values())[0])
    #         # tests_in_db.append(db_test)

    # for question in quiz["questions"]:
    #     db_question = crud.create_question(list(question.values())[0])
    #         # questions_in_db.append(db_question)
    #         # {'test_question': 'Over the last 2 weeks, how often have you been bothered by feeling, nervous, anxious or on edge?'}
    #         # keys = {'test_question'}


    # tests=crud.get_all_test()
    # questions=crud.get_all_questions()

    # for test in tests
        
    # db_test_question=crud.create_test_question(db_test, db_question)
    
for n in range(3):
    email = f"user{n}@test.com"  
    password = "test"
    name= f"testusername{n}"
    lname=f"testlastname{n}"
    user = crud.create_user(email, password, name, lname)