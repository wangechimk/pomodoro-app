from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SubmitField
from wtforms.validators import Required


class ActivityForm(FlaskForm):
    amount_time = IntegerField("Amount of time for the activity", validators=[Required()])
    break_time = IntegerField("Amount of time for  break", validators=[Required()])
    break_activity = TextAreaField("What activity will you do?", validators=[Required()])
    submit = SubmitField("Add activity")
