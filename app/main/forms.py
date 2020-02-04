from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_babel import lazy_gettext as _l


class EditProfileForm(FlaskForm):
    username = StringField(
        _l('Username'),
    )

    about_me = TextAreaField(
        _l('About me'),
        validators=[Length(min=0, max=140)]
    )

    submit = SubmitField()


class PostForm(FlaskForm):
    body = TextAreaField(
        _l('Enter something'),
        validators=[DataRequired(), Length(min=1, max=140)]
    )

    submit = SubmitField()
