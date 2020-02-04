import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()


def create_app(config_class=Config):
    e_app = Flask(__name__)
    e_app.config.from_object(config_class)

    db.init_app(e_app)
    migrate.init_app(e_app, db)
    login.init_app(e_app)
    mail.init_app(e_app)
    bootstrap.init_app(e_app)
    moment.init_app(e_app)
    babel.init_app(e_app)

    from app.errors.handlers import bp as errors_bp
    e_app.register_blueprint(errors_bp)

    from app.auth.routes import bp as auth_bp
    e_app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main.routes import bp as main_bp
    e_app.register_blueprint(main_bp)

    if not e_app.debug and not e_app.testing:

        if not os.path.exists('logs'):
            os.mkdir('logs')

        file_handler = RotatingFileHandler('logs/microblog.log',
                                           maxBytes=10240, backupCount=10)

        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))

        file_handler.setLevel(logging.INFO)
        e_app.logger.addHandler(file_handler)

        e_app.logger.setLevel(logging.INFO)
        e_app.logger.info('Microblog startup')

    return e_app


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])


from app import models
