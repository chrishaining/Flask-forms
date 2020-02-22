from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NewStudentForm(FlaskForm):
    first_name = StringField('Firstname')
    last_name = StringField('Lastname')
    submit = SubmitField('Submit')