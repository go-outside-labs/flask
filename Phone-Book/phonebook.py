#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__= "CI PhoneBook Manager"



import sys
import pickle
dbname = 'phonebook.pickle'


def create_db(dbname=dbname):
    db = {}

    with open(dbname, 'wb') as f:
        pickle.dump(db, f)

    print("New PhoneBook created.")




def add_entry(values, dbname=dbname):
    if len(values) != 2:
        print("Invalid number of arguments.")
        sys.exit(0)

    name = cleansing_name(values[0])
    phone = cleansing_phone(values[1])

    with open(dbname, 'rb') as f:
        db = pickle.load(f)

    db[name] = phone

    with open(dbname, 'wb') as f:
        pickle.dump(db, f)

    print("New entry added.")




def change_number(values, dbname=dbname):
    if len(values) != 2:
        print("Invalid number of arguments.")
        sys.exit(0)

    name = cleansing_name(values[0])
    newphone = cleansing_phone(values[1])


    with open(dbname, 'rb') as f:
        db = pickle.load(f)

    db[name] = newphone

    with open(dbname, 'wb') as f:
        pickle.dump(db, f)

    print name + " entry changed to " + newphone





def del_entry(values, dbname=dbname):
    if len(values) != 1:
        print("Invalid number of arguments.")
        sys.exit(0)

    name = cleansing_name(values[0])

    with open(dbname, 'rb') as f:
        db = pickle.load(f)

    del db[name]

    with open(dbname, 'wb') as f:
        pickle.dump(db, f)

    print name + " deleted"




def find_name(values, dbname=dbname):
    if len(values) != 1:
        print("Invalid number of arguments.")
        sys.exit(0)

    name = cleansing_name(values[0])

    with open(dbname, 'r+') as f:
        db = pickle.load(f)
        phone = db.get(name)

        if phone:
            print "Phone for " + name + " is " + phone
            return True
        else:
            print "Name not found."
            return False





def find_phone(values,dbname=dbname):
    if len(values) != 1:
        print("Invalid number of arguments.")
        sys.exit(0)

    phone = values[0]

    with open(dbname, 'rb') as f:
        db = pickle.load(f)

        try:
            name = (key for key,value in db.items() if value==phone).next()
            print "Name for " + phone + " is " + name
            return True
        except:
            print "Phone not found."
            return False




def cleansing_name(string):
    try:
        assert(len(string) < 30)
        return string.title()
    except:
        print("Name is too long. Try a shorter one.")
        sys.exit(0)




def cleansing_phone(string):
    try:
        assert(len(string) < 12)
        return string
    except:
        print("Phone number is too long. Try a shorter one.")
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
                ["create", "create_db()"]]

    for o in options:
        if option_input == o[0]:
            exec(o[1])
            sys.exit(0)


    print("Invalid option.")
    sys.exit(0)


if __name__ == '__main__':
    main()