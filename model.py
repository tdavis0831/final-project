from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	"""a user"""

	__tablename__= "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	password= db.Column(db.String(50))
	name=db.Column(db.String(50))
	lname=db.Column(db.String(50))
	
	def __repr__(self):
   
		return f"<user_id = {self.user_id} email={self.email}>"



class Test(db.Model):
	"""a test"""

	__tablename__="tests"

	test_id = db.Column(db.Integer, primary_key=True)
	test_name = db.Column(db.String (100))

	def __repr__(self):
		return f"<Test test_id={self.test_id} test_name={self.test_name}>"


class Question(db.Model):
	"""a question"""

	__tablename__= "questions"

	question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	question= db.Column(db.String, unique=True)


	def __repr__(self):
		return f"<Question question_id={self.question_id} question={self.question}>"


class TestQuestion(db.Model):
	"""a question that belongs to a test"""

	__tablename__= "test_questions"

	test_question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	fk_question_id = db.Column(db.Integer, db.ForeignKey("questions.question_id"))
	fk_test_id = db.Column(db.Integer, db.ForeignKey("tests.test_id"))
	# test_question = db.Column(db.String)
	# fk_user_test_question_answer_id = db.Column(db.Integer, db.ForeignKey("answers.user_test_question_answer_id"))
	# fk_test_question_rubric_id = db.Column(db.Integer, db.ForeignKey("rubrics.test_rubric_id"))

	test = db.relationship("Test", backref="test_questions")
	question = db.relationship("Question", backref="test_questions")
	
	# answer = db.relationship("UserTestQuestionAnswer", backref="questions")
	# rubric = db.relationship("TestQuestionRubric", backref ="questions")

	def __repr__(self):
		return f"<TestQuestion test_question_id={self.test_question_id} question_id={self.fk_question_id} test_id={self.fk_test_id}>"


class UserTestQuestionAnswer(db.Model):
	"""a user's answer to question"""

	__tablename__="answers"

	user_test_question_answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_test_question_answer = db.Column(db.Integer)
	fk_test_question_id = db.Column(db.Integer, db.ForeignKey("test_questions.test_question_id"))  
	fk_user_id=db.Column(db.Integer, db.ForeignKey("users.user_id"))                                                                                                             


	question=db.relationship("TestQuestion", backref="answers")
	user=db.relationship("User", backref="answers")

	def __repr__(self):
		return f"<test_answers = {self.user_test_question_answer}>"




class TestRubric(db.Model):

	__tablename__ = "rubrics"

	test_rubric_id =  db.Column(db.Integer, autoincrement=True, primary_key=True)
	test_rubric_healthy_baseline = db.Column(db.Integer)
	fk_test_id = db.Column(db.Integer, db.ForeignKey("tests.test_id"))
	
	test=db.relationship("Test", backref="rubrics")

	

 
	def __repr__(self):
		return f"<test_question_rubric_healthy_baseline  = {self.test_rubric_healthy_baseline }>"





def connect_to_db(flask_app, db_uri="postgresql:///quizzes", echo=False):
	flask_app.config["SQLALCHEMY_DATABASE_URI"] =  db_uri
	flask_app.config["SQLALCHEMY_ECHO"] = echo
	flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

	db.app = flask_app
	db.init_app(flask_app)

	print("Connected")

if __name__ == "__main__":
	from server import app

	# print(db.metadata.tables)



	connect_to_db(app)