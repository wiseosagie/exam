from flask_wtf import FlaskForm, Form
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, RadioField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from  guestbook.models import Register, Subject, subject_query, Test, Question, Answer
# from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class RegisterForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_email(self, email):
        user = Register.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email is taken, Please choose another email')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AddSubjectForm(FlaskForm):
    sub_name = StringField('Subject', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add Subject')

class AddTestForm(FlaskForm):
    sub_name = QuerySelectField(query_factory=subject_query, allow_blank=True, get_label = 'sub_name')
    test_name = StringField('Subject', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add Test')

class AddQuestionForm(FlaskForm):
    ques = StringField('Question', validators=[DataRequired(), Length(min=1, max=1000)])
    ans1 = StringField('Answer 1', validators=[DataRequired(), Length(min=1, max=1000)])
    ans2 = StringField('Answer 2', validators=[DataRequired(), Length(min=1, max=1000)])
    ans3 = StringField('Answer 3', validators=[DataRequired(), Length(min=1, max=1000)])
    ans4 = StringField('Answer 4', validators=[DataRequired(), Length(min=1, max=1000)])
    true_ans = StringField('true_ans', validators=[DataRequired(), Length(min=1, max=2)])
    submit = SubmitField('Add Question')

class AnswerForm(Form):
    your_answer = RadioField("", choices=[('ans1', 'ans1'),('ans2','q.ans2'), ('ans3','q.ans3'), ('ans4','q.ans4')])
    example = RadioField('Label', choices=[('value','description'),('value_two','whatever')])
    submit = SubmitField('Answer')

class SimpleForm(Form):
    ans = 'ddd'
    # example = RadioField('Gender', choices = [('M','Male'),('F','Female')])
    # Age = IntegerField("age")
    example = RadioField("example", choices=[(ans, 'ans'),('ans2','q.ans2'), ('ans3','q.ans3'), ('ans4','q.ans4')])
    # ('Label', choices=[('value','description'),('value_two','whatever')])
    submit = SubmitField('Answer')
