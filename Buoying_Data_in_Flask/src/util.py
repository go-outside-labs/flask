# -*- coding: utf-8 -*-
"""

This module contains util methods than can be used by all the other classes.

"""

import yaml


def read_config_file():
    ''''
        Read the YAML config file and return it as a dictionary.
    '''
    config_file =  "./config.yaml"

    try:
        with open(config_file, 'r') as f:
            return yaml.load(f)

    except yaml.YAMLError as e:
        print("Error opening {0}: {1}".format(config_file, e))