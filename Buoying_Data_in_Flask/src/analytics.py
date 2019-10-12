# -*- coding: utf-8 -*-
"""

This module parses, analyses, and returns NDBC feed's data.

Todo:
    * Add an option for the user to customize miles, longitude and latitude
            inside the NDBC_URL (instead of having it from config.yaml).
    * Add more in-depth inspection for the feed data, and turn the method into
            a proper class.
    * Nice to have: implement feedparser work on bs4 to make everything more
            uniform.

"""
import sys

from feedparser import parse
from bs4 import BeautifulSoup

from helpers import read_config_file


def parse_lxml_data(data, tag="strong"):
    '''
        Given some LXML data to be parsed based in a given tag,
        returns it in a dictionary.
    '''
    bs = BeautifulSoup(data, "lxml")

    # Clean up any extra tag from the data.
    for e in bs.findAll('br'):
        e.extract()

    # Create a dict entry for each entry in the data.
    aux_dict = {}
    for tag in bs.find_all(tag):
        key = tag.text.strip(':')
        value = tag.next_sibling
        aux_dict[key] = value

    aux_list = []
    for key, value in aux_dict.items():
        aux_list.append(key + ": " + value)

    return aux_list


def get_stations_list():
    '''
        Given an encoded and crafted NDBC_URL, parse its feed data, using
        the feedparser library.
    '''

    # Get coordinates information from the config file.
    config = read_config_file()
    try:
        url = config['NDBC_URL']
        lat = config['LAT']
        lon = config['LON']
        rad = config['RAD']
        show_ships = config['SHOW_SHIPS']

    except KeyError:
        print("Config file is ill-formatted.")
        sys.exit(1)

    # Get the feed data dump from the customized NDBC url.
    url = url.format(lat, lon, rad)
    feed = parse(url)

    # Parse the feed data.
    stations = []

    for entry in feed.entries:

        if entry.title == "SHIP" and not show_ships:
            continue

        station_data= {}

        station_data['name'] = entry.title
        station_data['id'] = entry.id
        station_data['coordinates'] = entry.where['coordinates']
        station_data['data'] = parse_lxml_data(entry.summary_detail.value)

        stations.append(station_data)

    return stations