# -*- coding: utf-8 -*-
"""

In this module we use WTForms, a module for validation of forms.
We use its built-in validator StringField for our data.

Todo:
    * Enforcer username policy for min=3 and add validation on signup
            route in app.py.
    * Make email an optional field (after we are validating it as
            a unique key in app.py).
    * Validate email format.
    * Improve password policy for min=8 after adding password policy
            enforcing in helpers.py.

"""

from wtforms import Form, StringField, validators

class LoginForm(Form):
    """
        Form validation for the users database and form.
    """
    username = StringField(u'Username:', validators=[validators.required(), validators.Length(min=1, max=30)])
    password = StringField(u'Password:', validators=[validators.required(), validators.Length(min=1, max=30)])
    email = StringField(u'Email:', validators=[validators.optional(), validators.Length(min=0, max=50)])


class Station(Form):
    """
        Form validation for the stations database and form.
    """
    name = StringField(u'Name:', validators=[validators.required(), validators.Length(min=3, max=100)])
    station_id = StringField(u'ID:', validators=[validators.required(), validators.Length(min=3, max=100)])
