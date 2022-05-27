from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPet(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired(message="Must enter pet's name")])
    species = StringField('Pet Species', validators=[InputRequired(message="Please enter pet's species"), AnyOf(values=['Cat','Dog', 'Porcupine'], message='We only accept dogs, cats, and porcupines')])
    age = IntegerField('Pet Age', validators=[NumberRange(min=0, max=30)])
    photo_url = StringField('Photo of Pet',validators=[URL(require_tld=False), Optional()])
    notes = StringField('Notes')
    available = SelectField('Available', validators=[InputRequired(message='Must provide if pet is available to adopt')])