from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Main (FlaskForm):
    button =  SubmitField('')

    

class UsersRegister (FlaskForm):
    username = StringField('Enter username')
    submit = SubmitField("Create")


class UsersSearch (FlaskForm):
    username = StringField('Enter username')
    submit = SubmitField("Search")

 

 