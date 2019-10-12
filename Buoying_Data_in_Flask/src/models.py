# -*- coding: utf-8 -*-
"""

This module define the logical structure of our databases and determines
in which manner data will be stored, organized and manipulated.

Todo:
    * Create classes that model and connections so that the
            code will be more robust in app.py and helpers.py.
    * Validate email as an unique string in the User class/database.
    * Add more detailed fields for data in the Stations class/database.

"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from util import read_config_file


"""
    Factory function that constructs a base class for declarative class
    definitions (which is assigned to Base variable).
"""
Base = declarative_base()

def db_connect():
    '''
        Method for database creation and connection using predefined
        database settings.
    '''
    db_url = read_config_file()
    return create_engine(db_url['SQLALCHEMY_DATABASE_URI'])


"""
    Database Classes.
"""

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    password = Column(String(30))
    email = Column(String(50))

    def __repr__(self):
        return '<User {0}>'.format(self.name)


class Stations(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True)
    station_id = Column(String(30))
    user = Column(String(30))
    name = Column(String(30))
    coordinates = Column(String(50))
    data = Column(String(500))

    def __repr__(self):
        return '<Station {0}>'.format(self.name)


"""
    Connect to database and create models.
"""
engine = db_connect()
Base.metadata.create_all(engine)
