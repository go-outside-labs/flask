# -*- coding: utf-8 -*-
"""

This module contains database helper methods.


Todo:
    * Add methods and routes to delete entries in the database.
    * Create classes that model and connections in models.py so engine
            and Base can be imported from there.
    * Adding logging levels to STDOUT/ERR.
    * Do a Join table/relationship instead of querying on the session user
            (for better persistence and scalability).
    * Compress is_user_key_take() and is_stations_key_take() in on method.

"""

import bcrypt

from flask import session
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, join
from sqlalchemy.exc import IntegrityError, InvalidRequestError

from models import User, Stations, db_connect, Base, engine
from util import read_config_file


Base.metadata.create_all(db_connect())

"""
    User session helper methods, supported by SQLAlchemy.
"""
@contextmanager
def session_scope():
    '''
        Provide a transactional scope for user operations.
    '''
    s = get_session()
    s.expire_on_commit = False

    try:
        yield s
        s.commit()

    except:
        s.rollback()
        raise

    finally:
        s.close()


def get_session():
    '''
        Create the current session.
    '''
    return sessionmaker(bind=engine)()


def get_user():
    '''
        Get the user for the current session.
    '''
    name = session['name']

    with session_scope() as s:
        user = s.query(User).filter(User.name.in_([name])).first()

    return user


"""
    User password helper methods.
"""
def hash_password(password):
    '''
        Hash the password with BCrypt (Blowfish block cipher cryptomatic
        algorithm, in form of an adaptive hash function), before sending
        it to the database.
    '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def credentials_valid(name, password):
    '''
        Retrieve the hashed password from the database for comparison.
    '''
    with session_scope() as s:
        user = s.query(User).filter(User.name.in_([name])).first()

        if user:
            return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

        return False

"""
    Database helper methods.
"""
def is_user_key_take(name):
    '''
        Verify whether a key already exists in the database.
    '''
    with session_scope() as s:
        return s.query(User).filter(User.name.in_([name])).first()


def is_station_key_take(name):
    '''
        Verify whether a key already exists in the database.
    '''
    with session_scope() as s:
        return s.query(Stations).filter(Stations.name.in_([name])).first()


def add_station(station_name, station_id, coordinates, data):
    '''
        Add a station entry to the Stations DB.
    '''
    station = Stations(user=session['name'], station_id=station_id, name=station_name, \
        coordinates=coordinates, data=data)

    with session_scope() as s:
        if not is_station_key_take(station.name):
            s.add(station)
            s.commit()
            return True

        else:
            print("{0} is already in the database.".format(station.name))
            return False


def add_user(name, password, email):
    '''
        Add a user entry to the Users DB.
    '''
    user = User(name=name, password=password, email=email)

    with session_scope() as s:
        if not is_user_key_take(user.name):
            try:
                s.add(user)
                s.commit()

            except IntegrityError:
                print("Could not add {0} to database.".format(user.name))

            except InvalidRequestError:
                print("Could not add data for {0} to database.".format(user.name))

        else:
            print("{0} is already in the database.".format(user.name))


def get_favorites():
    '''
        Return all the favorite sessions.
    '''
    with session_scope() as s:
        return s.query(Stations).filter(Stations.user == session['name']).all()
