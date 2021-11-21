
"""Crud operations"""

from model import db, User, Test, TestQuestion, Question, TestRubric, UserTestQuestionAnswer, connect_to_db
# TestQuestion, UserTestQuestionAnswer, TestQuestionRubric,



def create_rubric(test_rubric_healthy_baseline, test):
    
    rubric=TestRubric(test_rubric_healthy_baseline=test_rubric_healthy_baseline, test=test)
    db.session.add(rubric)
    db.session.commit()




def create_user(email, password, name, lname):
    #creates a user

    user=User(email=email, password=password, name=name, lname=lname)
    
    db.session.add(user)
    db.session.commit()

    return user


def create_test(test_name):
    #creates a test
    
    test=Test(test_name=test_name)

    db.session.add(test)
    db.session.commit()

    return test

def create_question(question):

    question=Question(question=question)

    db.session.add(question)
    db.session.commit()

    return question

def create_test_question(test, question):

    # test1 is a test object that is being passed into TestQuestion object
    # constructor as the argument for the db.relationship 'test'

    # question1 is a test object that is being passed into TestQuestion object
    # constructor as the argument for the db.relationship 'question'

    test_question=TestQuestion(test=test, question=question)
    
    db.session.add(test_question)
    db.session.commit()

    return test_question

def get_all_tests():
    return db.session.query(Test).all()

def get_all_questions(): 
  
    question_list=[]
    question_set=(db.session.query(Question.question).all())
    for question in question_set:
        question_list.append(question[0])
    return question_list

def get_anxiety_questions():
    anxiety_questions=[]
    question_set=db.session.query(TestQuestion).filter(TestQuestion.fk_test_id ==1).all() #gets a list of objects where test_id =1 (anxiety)
    
    # return question_set
    for test_question in question_set:
        anxiety_questions.append(test_question.question)
    
    return anxiety_questions

# def get_anxiety_answers():
#     anxiety_answers_list=[]
#     anxiety_answers=db.session.query(UserTestQuestionAnswer).filter(UserTestQuestionAnswer.fk_test_question_id > 0).all()
    
#     for answer in anxiety_answers:
#         anxiety_answers_list.append(answer.question)
#     return anxiety_answers_list

def get_depression_questions():
    depression_questions=[]
    question_set=db.session.query(TestQuestion).filter(TestQuestion.fk_test_id == 2).all() 

    for test_question in question_set:
        depression_questions.append(test_question.question)
    
    return depression_questions

def get_insomnia_questions():
    insomnia_questions=[]
    question_set=db.session.query(TestQuestion).filter(TestQuestion.fk_test_id ==3).all() 

    for test_question in question_set:
        insomnia_questions.append(test_question.question)
    
    return insomnia_questions
def get_rubric():
    rubrics= db.session.query(TestRubric).filter(TestRubric.fk_test_id==1).first()

    return rubrics.test_rubric_healthy_baseline


def get_rubric_depression():
    rubrics= db.session.query(TestRubric).filter(TestRubric.fk_test_id==2).first()

    return rubrics.test_rubric_healthy_baseline


def get_rubric_insomnia():
    rubrics= db.session.query(TestRubric).filter(TestRubric.fk_test_id==3).first()

    return rubrics.test_rubric_healthy_baseline

def get_anxiety_results():
    a_results= db.session.query(UserTestQuestionAnswer).filter(UserTestQuestionAnswer.fk_test_id == 1).all()

    print(a_results)

    
def user_answer(user_test_question_answer, fk_test_question_id,fk_user_id):

    
    
    user_answer=UserTestQuestionAnswer(user_test_question_answer=user_test_question_answer, 
                                        fk_test_question_id=fk_test_question_id ,fk_user_id=fk_user_id)


    db.session.add(user_answer)
    db.session.commit()

    return user_answer

def user_total(answer_list, question_id_list,fk_user_id):
    user_sum = 0
    for i in range(len(answer_list)):
        user_sum+=answer_list[i]


    return user_sum

def user_nums(answer_list, question_id_list,fk_user_id):
    answer_info=[]
    for i in range(len(answer_list)):
       answer_info.append(answer_list[i])

        

    return answer_info

def check_for_answer(question, user):
    question_id_check= db.session.query(UserTestQuestionAnswer).filter(
        UserTestQuestionAnswer.fk_test_question_id == question.test_question_id 
        ).filter(
         user.user_id == UserTestQuestionAnswer.fk_user_id
        ).all()
    return len(question_id_check) > 0


 
def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()   


    
    # print(test1)
    # question_set=(db.session.query(TestQuestion).filter(TestQuestion.fk_question_id).all())
    # print(question_set) 

    # for question in question_set:
    #         question_list.append(question)
    # print(question_list)
   

    
    # for question in question_set:
    #     question_list.append(question[0])

        

   
    


# def get_test_by_id

# def create_user_test_answer(user, test, question, user_test_question_answer):
#     answer=UserTestQuestionAnswer( user=user, test=test, question=question, 
#     user_test_question_answer=user_test_question_answer)

#     db.session.add(answer)
#     db.session.commit()

#     return answer



if __name__ == "__main__":
    from server import app

    connect_to_db(app)