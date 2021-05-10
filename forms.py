from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email, DataRequired

class SignUpForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    CourseName = StringField('CourseName',
    					validators=[DataRequired()])
    CourseNumber = StringField('CourseNumber',
    					validators=[DataRequired()])
    CourseSection = StringField('CourseSection',
    					validators=[DataRequired()])
    submit = SubmitField('Sign Up')