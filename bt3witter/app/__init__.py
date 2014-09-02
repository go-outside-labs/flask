# This script simply creates the application object of class Flask
# and then import the views and models modules.
#
# The view are handlers that respond to requests from the web browsers.
# Each view function is mapped to one or more request URLs.


from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views