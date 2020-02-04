from app import create_app, db, cli
from app.models import User, Post

e_app = create_app()
cli.register(e_app)


@e_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
