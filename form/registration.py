from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Registration(FlaskForm):
    first_name = StringField("First Name:", validators=[DataRequired()])
    last_name = StringField("Last Name:", validators=[DataRequired()])
    middle_name = StringField("Middle Name:")
    phone_number = StringField("Phone Number:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired()])
    mobile_number = StringField("Mobile Number:", validators=[DataRequired()])
    gender = StringField("Gender:")
    height = StringField("Height:")
    weight = StringField("Weight:")
    age = StringField("Age:")
    nationality = StringField("Nationality:")

    submit = SubmitField('submit')
