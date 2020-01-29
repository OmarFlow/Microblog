from app import e_app, db
from app.models import User, Post
from app import cli

@e_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}