from flask import Flask, render_template, url_for, flash, redirect, request
from guestbook import app, db, bcrypt
from guestbook.form import RegisterForm, LoginForm, AddSubjectForm, AddTestForm, AddQuestionForm, AnswerForm, SimpleForm
from guestbook.models import User, Register, Subject, subject_query, Test, Question, Answer
from flask_login import login_user, current_user, logout_user, login_required
from  sqlalchemy.sql.expression import func, select




posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = Register(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='account')

# Subject Creation
@app.route('/add_subject', methods=['GET', 'POST'])
@login_required
def add_subject():
    subjects = Subject.query.all()
    form = AddSubjectForm()
    if form.validate_on_submit():
            addSubject = Subject(sub_name=form.sub_name.data)
            db.session.add(addSubject)
            db.session.commit()
            flash('Your Subject has been created!', 'success')
            return redirect(url_for('home'))
    return render_template('add_subject.html', title='Add Subject', form=form, subjects=subjects)

# Test Creation
@app.route('/add_test', methods=['GET', 'POST'])
@login_required
def add_test():
    form = AddTestForm()
    if form.validate_on_submit():
            addTest = Test(sub_name=form.sub_name.data.sub_name, test_name = form.test_name.data)
            db.session.add(addTest)
            db.session.commit()
            flash('Your Test has been created!', 'success')
            return redirect(url_for('home'))
    return render_template('add_test.html', title='Add Test', form=form)

# Question Creation
@app.route('/add_questions', methods=['GET', 'POST'])
@login_required
def add_question():
    form = AddQuestionForm()
    if form.validate_on_submit():
        AddQuestion = Question(ques=form.ques.data, ans1 = form.ans1.data, ans2 = form.ans2.data, ans3 = form.ans3.data, ans4 = form.ans4.data, your_ans = form.true_ans.data)
        db.session.add(AddQuestion)
        db.session.commit()
        flash('Your Questions has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('add_questions.html', title='Add Question', form=form)

@app.route('/question', methods=['GET', 'POST'])
@app.route('/question/page/<int:page>', methods=['GET', 'POST'])
def question(page=1):
    # questions = Question.query.paginate(page, per_page=1)
    quess = Question.query.order_by(func.rand())
    quest = quess.limit(3).from_self()
    questions = quest.paginate(page, per_page=1)
    print('new1')

    form = AnswerForm(request.form)
    # form = request.get("your_answer")
    # radio_value = form.your_answer

    

    if request.method == 'POST':
        # ans = request.get("your_answer")

        print "submitted"
        print form.your_answer.data
        print "news"
        # print form.ans
        print "space"
        # print form.radio_value


    return render_template('questionview.html', title=' Quiz', questions=questions, form=form)

@app.route('/testpage',methods=['post','get'])
def testpage():
    form = SimpleForm(request.form)
    if form.submit():
        print (form.example.data)
    else:
        print form.errors
    return render_template('testpage.html',form=form)
