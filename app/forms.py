from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CSRFProtect

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
