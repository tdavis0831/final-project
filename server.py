"""Server for movie questionaires"""
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "fvdrgdtuntryktuit8578r6bw345vwv"
app.jinja_env.undefined = StrictUndefined



@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/create-account")
def create_account():

    return render_template("create-account.html")





    

    # user_answer= crud.user_total()

    return redirect("/results")


# @app.route("/answers", methods=["GET"])
# def show_results():
#     answers = request.form.getlist("answer")


#     return render_template("results.html", answers=answers)
    


#     return render_template("results.html", user_answer=user_answer)



@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Email already associated with account, try logging in")
    else:
        crud.create_user(email, password)
        flash("Account created! Please log in.")

    return redirect("/")

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's id in session
        session["user_id"] = user.user_id
        

    return render_template("user-profile.html")



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

    print(fk_test_question_id)
    print(user_test_question_answer)
    print(session["user_id"])
    answers=crud.user_total(user_test_question_answer, fk_test_question_id,fk_user_id)
    baselines=crud.get_rubric()
    print(baselines)
    # return answers
        
    
    # print("added")
    return render_template("results.html", answers=answers, baselines=baselines)




@app.route("/anxiety")
def anxiety_questionnaire():

    if "user_id" not in session:
        return redirect("/") 

    anxiety_questions = crud.get_anxiety_questions()
    return render_template("anxiety.html", question=anxiety_questions)




    
    



@app.route("/depression")
def depression_questionnaire():

    depression_questions = crud.get_depression_questions()

    return render_template("depression.html", question=depression_questions)

@app.route("/insomnia")
def insomnia_questionnaire():

    insomnia_questions = crud.get_insomnia_questions()

    return render_template("insomnia.html", question=insomnia_questions)

# @app.route("/users", methods=["POST"])
# def register_user():
#     """Create a new user."""

#     email = request.form.get("email")
#     password = request.form.get("password")

#     user = crud.get_user_by_email(email)
#     if user:
#         flash("Cannot create an account with that email. Try again.")
#     else:
#         crud.create_user(email, password)
#         flash("Account created! Please log in.")

# @app.route("?", methods=["POST"])

# def user_answer("""TESTQUESTION ID"""):

#     emailed_logged_in = session.get("user_email")
#     answer_by_user = request.form.get("answer")







if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
    