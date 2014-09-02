__author__ = "Marina Wahl"

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

# LoginForm knows renders form fields as HTML
class LoginForm(Form):
    # the Required import is a validator, a function that can be
    # attached to a field to perform validation of data. Required
    # checks that the field is not empty.
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)