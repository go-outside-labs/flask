# -*- coding: utf-8 -*-
"""

This module is the entry point of our app.

Example:
    To run the app in developer mode, run the follow after installing
    all the dependences:

        $ python app.py


Todo:
    * Add settings view.
    * Add recovery password methods.
    * Validate email a unique key.
    * Add support for confirmation email.
    * Create classes that model and connections in models.py so engine
            and Base can be imported from there.

"""
import os
import json

from flask import Flask, redirect, url_for, render_template, request, session
from forms import LoginForm

from analytics import get_stations_list
from models import User, Stations, db_connect, Base
from helpers import read_config_file, credentials_valid, get_user, hash_password, \
                is_user_key_take, add_station, add_user, get_favorites


"""
    This is how Flask creates models and and connects to the database.
"""
app = Flask(__name__)
engine = db_connect()
Base.metadata.create_all(engine)


"""
    The follow methods indicate the routes for each view in the view.
"""
@app.route('/', methods=['GET', 'POST'])
def login():
    '''
        Log out view, redirecting to the RSS list page.
    '''
    if not session.get('logged_in'):

        form = LoginForm(request.form)
        if request.method == 'POST':

            name = request.form['username'].lower()
            password = request.form['password']

            if form.validate():
                if credentials_valid(name, password):

                    session['logged_in'] = True
                    session['name'] = name
                    return json.dumps({'status': 'Login successful'})

                else:
                    return json.dumps({'status': 'Invalid user/pass'})

            else:
                return json.dumps({'status': 'All fields required'})

        elif request.method == 'GET':
            return render_template('index.html', form=form)

    # Once user is auth-ed, opens RSS feed for stations.
    return render_template('home.html', stations_list=get_stations_list(), user=get_user())


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    '''
        Log out view, redirecting to the main page.
    '''
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
        Sign up view for new users, redirecting to  the RSS list page.
    '''
    if not session.get('logged_in'):

        form = LoginForm(request.form)

        if request.method == 'POST':

            username = request.form['username'].lower()
            password = hash_password(request.form['password'])
            email = request.form['email']

            if form.validate():

                if not is_user_key_take(username):

                    add_user(username, password, email)
                    session['logged_in'] = True
                    session['name'] = username
                    return json.dumps({'status': 'Signup successful'})

                return json.dumps({'status': 'Username taken'})

            return json.dumps({'status': 'User/Pass required'})

        return render_template('index.html', form=form)

    return redirect(url_for('login'))


@app.route('/favorites', methods=['GET'])
def favorites():
    '''
        Show list of favorite stations.
    '''
    return render_template('favorites.html', fav_stations=get_favorites())


@app.route('/stations', methods=['POST', 'GET'])
def stations():
    '''
        Show RSS station list.
    '''
    if request.method == 'POST':

        try:
            name, station_id, coordinates, data = request.form['results'].split(';')
            result = add_station(name, station_id, coordinates, data)

            if result:
                info = "Station {0} was added to favorites.".format(name)

            else:
                info = "Station {0} is already in your favorites.".format(name)

            return render_template('stations.html', info=info)

        except Exception as e:
            return render_template('error.html', error=str(e))

    return redirect(url_for('login'))


if __name__ == "__main__":

    config = read_config_file()
    SECRET_KEY = os.urandom(12)
    app.secret_key =  SECRET_KEY

    app.run(host=config['HOST'], port=config['PORT'], \
            debug=config['DEBUG_MODE'], use_reloader=config['USE_RELOADER'])

