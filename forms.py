#forms.py
from ast import Str
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy:  ')
    submit = SubmitField('Add Puppy')


    
class DelForm(FlaskForm):
    id = IntegerField("Id Number of Puppy to Remove:" )
    submit = SubmitField('Remove Puppy')

class AddOwnerForm(FlaskForm):
    owner_name = StringField('Name of the Owner:  ')
    pup_id = IntegerField('Id of Puppy')
    submit_owner = SubmitField('Add Owner')