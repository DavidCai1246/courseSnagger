from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email, DataRequired

class SignUpForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    CourseNumber = StringField('CourseNumber')
    CourseSectionNumber = StringField('CourseSectionNumber')
    submit = SubmitField('Sign Up')