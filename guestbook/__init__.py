from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'jekhrluiwhu5h489545nfn945'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/exam'
 # 'mysql://sql9285155:IvMQfGLZ5c@sql9.freemysqlhosting.net/sql9285155'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from guestbook import routes
