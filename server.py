"""Server for final project"""
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import api
import random

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "fsdgsdfgsgf"
app.jinja_env.undefined = StrictUndefined

AFFIRMATIONS = [
    "There are people out there who will help me.",
    "How I feel matters.",
    "I am happy to be me.",
    "I matter.",
    "I love myself for who I am.",
    "I am worthy of love and happiness.",
    "I treat myself with love and kindness.",
    "My feelings are valid.",
    "I deserve all the happiness in the world.",
    "Reaching out for support shows strength.",
    "I am allowed to have mental health struggles."


]


@app.route('/affirmations')
def fortune():
    """Return a single fortune as a text string (*not* the whole HTML page!)"""

    return random.choice(AFFIRMATIONS)

@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/create-account")
def create_account():

    return render_template("create-account.html")

@app.route("/resources")
def resources():

    return render_template("assessmentinfo.html")


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")
    name= request.form.get("name")
    lname=request.form.get("lname")

    user = crud.get_user_by_email(email)
    
    if user:
        flash("Email already associated with account, try logging in")
    else:
        crud.create_user(email, password, name, lname)
        flash("Account created! Please log in.")

    return redirect("/")






@app.route("/login", methods=["POST", "GET"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")
    name=request.form.get("name")
    lname=request.form.get("lname")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's id in session
        session["user_id"] = user.user_id
        session["name"] = user.name
        
        

    return render_template("user-profile.html", user=user)





@app.route("/anxiety")
def anxiety_questionnaire():

    if "user_id" not in session:
        return redirect("/") 

    anxiety_questions = crud.get_anxiety_questions()
    
    
    return render_template("anxiety.html", question=anxiety_questions)





@app.route("/depression")
def depression_questionnaire():
    
    if "user_id" not in session:
        return redirect("/") 
    depression_questions = crud.get_depression_questions()

    return render_template("depression.html", question=depression_questions)



@app.route("/answers", methods=["POST"])
def get_user_answers():

    user_key=[]
    user_values=[]

    # session["user_id"] = user.user_id
    # answers = request.form.getlist("answer")  #gets list of answers
    
    question_info={}
    fk_user_id= session["user_id"] 

    for k,v in request.form.items():
        question_info[k]= v 

    
    fk_test_question_id=list(question_info.keys())
    fk_test_question_id=[int(i) for i in fk_test_question_id]




    user_test_question_answer=list(question_info.values())
    user_test_question_answer=[int(i) for i in user_test_question_answer]

    


    
    # print(user.user_id)

    print()
    print(user_test_question_answer)
    print(session["user_id"])
    answers=crud.user_total(user_test_question_answer, fk_test_question_id,fk_user_id)
    individual_answers=crud.user_nums(user_test_question_answer, fk_test_question_id,fk_user_id)
    anxiety_questions = crud.get_anxiety_questions()
    baselines=crud.get_rubric()
    print(baselines)
    # return answers
        
    
    # print("added")
    return render_template("results.html", answers=answers, baselines=baselines, individual_answers=individual_answers, anxiety_questions=anxiety_questions)


@app.route("/depression_answers", methods=["POST"])
def get_user_answers_dep():
    
    
    if "user_id" not in session:
        return redirect("/") 
    user_key=[]
    user_values=[]

    # session["user_id"] = user.user_id
    # answers = request.form.getlist("answer")  #gets list of answers
    
    question_info={}
    fk_user_id= session["user_id"] 

    for k,v in request.form.items():
        question_info[k]= v 

   
    fk_test_question_id=list(question_info.keys())
    fk_test_question_id=[int(i) for i in fk_test_question_id]




    user_test_question_answer=list(question_info.values())
    user_test_question_answer=[int(i) for i in user_test_question_answer]

    


    
    # print(user.user_id)

    print(fk_test_question_id)
    print(user_test_question_answer)
    print(session["user_id"])
    individual_answers=crud.user_nums(user_test_question_answer, fk_test_question_id,fk_user_id)
    depression_questions=crud.get_depression_questions()
    answers=crud.user_total(user_test_question_answer, fk_test_question_id,fk_user_id)
    baselines=crud.get_rubric_depression()
    print(baselines)
    # return answers
        
    
    # print("added")
    return render_template("dresults.html", answers=answers, baselines=baselines, depression_questions=depression_questions, individual_answers=individual_answers)



@app.route("/therapist", methods=["POST"])
def find_therapist():
    city= request.form.get("city")
    provider_list = api.get_therapist_info(city)
    return render_template("therapist.html", provider_list=provider_list)




@app.route("/therapist")
def therapist_list():
    # provider_list = api.get_therapist_info()
    # print(provider_list)
    # print(type(provider_list))
    return render_template("therapist.html", provider_list=[])




    
@app.route("/insomnia")
def insomnia_questionnaire():
    
    if "user_id" not in session:
        return redirect("/") 
    insomnia_questions = crud.get_insomnia_questions()

    return render_template("insomnia.html", question=insomnia_questions)



@app.route("/insomnia_answers", methods=["POST"])
def get_user_answers_ins():

    user_key=[]
    user_values=[]

    question_info={}
    fk_user_id= session["user_id"] 

    for k,v in request.form.items():
        question_info[k]= v 

   
    fk_test_question_id=list(question_info.keys())
    fk_test_question_id=[int(i) for i in fk_test_question_id]




    user_test_question_answer=list(question_info.values())
    user_test_question_answer=[int(i) for i in user_test_question_answer]
    
    # print(user.user_id)
    print(question_info)
    print(fk_test_question_id)
    print(user_test_question_answer)
    print(session["user_id"])
    individual_answers=crud.user_nums(user_test_question_answer, fk_test_question_id,fk_user_id)
    insomnia_questions=crud.get_insomnia_questions()
    answers=crud.user_total(user_test_question_answer, fk_test_question_id,fk_user_id)
    baselines=crud.get_rubric_insomnia()
    print(baselines)
    # return answers
        
    
    # print("added")
    return render_template("iresults.html", answers=answers, baselines=baselines, insomnia_questions=insomnia_questions, individual_answers=individual_answers)


@app.route('/logout')
def process_logout():
    """Remove user from session"""

    if 'user' in session:
        session.pop('user', None)
        flash('You have successfully logged out.')
    else:
        flash('You are not logged in.')

    return render_template('homepage.html')


@app.route("/map")
def get_map():

    return render_template("map.html")


@app.route("/about")
def get_about():

    return render_template("about.html")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)