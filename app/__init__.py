from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel
from flask_babel import lazy_gettext as _l

from config import Config

e_app = Flask(__name__)
e_app.config.from_object(Config)
mail = Mail(e_app)

login = LoginManager(e_app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')

bootstrap = Bootstrap(e_app)

moment = Moment(e_app)
babel = Babel(e_app)

db = SQLAlchemy(e_app)
migrate = Migrate(e_app, db)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(e_app.config['LANGUAGES'])

from app import routes, models
