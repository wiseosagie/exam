from datetime import datetime
from guestbook import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Register.query.get(int(user_id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = True, nullable=False)
    email = db.Column(db.String(80), unique = True, nullable=False)
	# passw = db.Column(db.String(80), unique= False)
	# password = db.Column(db.String(180))

class Register(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180), unique = True, nullable=False)
    email = db.Column(db.String(180), unique = True, nullable=False)
    password = db.Column(db.String(180), nullable=False)

    def __repr__(self):
        return "Register('{self.name}')"

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_name = db.Column(db.String(180), nullable=False)

def subject_query():
    print('test')
    print(Subject.query)
    print('test')
    return Subject.query
    # .with_entities(Subject.sub_name)
    # filter_by(sub_name)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_name = db.Column(db.String(180), nullable=False)
    test_name = db.Column(db.String(180), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ques = db.Column(db.String(180), nullable=False)
    ans1 = db.Column(db.String(180), nullable=False)
    ans2 = db.Column(db.String(180), nullable=False)
    ans3 = db.Column(db.String(180), nullable=False)
    ans4 = db.Column(db.String(180), nullable=False)
    true_ans = db.Column(db.String(180), nullable=False)

def question_query():
    print('question')
    print(Question.query)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ques = db.Column(db.String(180), nullable=False)
    ans1 = db.Column(db.String(180), nullable=False)
    ans2 = db.Column(db.String(180), nullable=False)
    ans3 = db.Column(db.String(180), nullable=False)
    ans4 = db.Column(db.String(180), nullable=False)
    true_ans = db.Column(db.String(180), nullable=False)
