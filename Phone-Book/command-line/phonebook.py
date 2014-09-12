#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__= "CI PhoneBook Manager"



import os.path
import sys


def create_db(values):
    if len(values) != 1:
        print("Invalid number of arguments.")
        sys.exit(0)

    dbname = values[0]
    cleansing_dbname(dbname)

    dbname = dbname + '.db'

    try:
        with open(dbname, 'a') as f:
            f.write("# NAME     PHONE\n")
    except:
        print("DB cannot be created. Exiting.")
        sys.exit(0)


def add_entry(values):
    if len(values) != 2:
        print("Invalid number of arguments.")
        sys.exit(0)

    name, phone = values[0], values[1]
    cleansing_name(name)
    cleansing_phone(phone)

    print name, phone


def change_number(values):
    if len(values) != 2:
        print("Invalid number of arguments.")
        sys.exit(0)

    name, phone = values[0], values[1]
    cleansing_name(name)
    cleansing_phone(phone)

    print name, phone


def del_entry(values):
    if len(values) != 1:
        print("Invalid number of arguments.")
        sys.exit(0)

    name = values[0]
    cleansing_name(name)

    print name


def find_name(values):
    if len(values) != 1:
        print("Invalid number of arguments.")
        sys.exit(0)

    name = values[0]
    cleansing_name(name)

    print name


def find_phone(values):
    if len(values) != 1:
        print("Invalid number of arguments.")
        sys.exit(0)

    phone = values[0]
    cleansing_name(phone)

    print phone



def cleansing_name(string):
    try:
        assert(len(string) < 30)
    except:
        print("Name is too long. Try a shorter one.")
        sys.exit(0)


def cleansing_phone(string):
    try:
        assert(len(string) < 12)
    except:
        print("Phone number is too long. Try a shorter one.")
        sys.exit(0)


def cleansing_dbname(string):
    try:
        assert(len(string) < 10)
    except:
        print("Database name is too long. Try a shorter one.")
        sys.exit(0)



"""
    Main function & Menu
"""
def main():

    arguments = sys.argv[1:]

    try:
        option_input = arguments[0]
        values = arguments[1:]
    except:
        print("You need to give an option.")
        sys.exit(0)


    options =  [["add", 'add_entry(values)'], \
                ["change",  'change_number(values)'], \
                ["remove",  'del_entry(values)'], \
                ["find_num",  'find_phone(values)'], \
                ["find",  'find_name(values)'],\
                ["create", "create_db(values)"]]

    for o in options:
        if option_input == o[0]:
            exec(o[1])
            sys.exit(0)


    print("Invalid option.")
    sys.exit(0)


if __name__ == '__main__':
    main()