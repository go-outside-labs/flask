#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__= "This is the main file for our version\
                control. Everything runs from here."



import time
import os
import os.path
import sys

import system_operations, snapshot, checkout, metadata
from constants import BACKUP_DIR, CONTEND_DIR, CONFIG_FILE


# TODO: branches
# TODO: make the checkout diff to optmize/make it safer (instead of deleting the folder)
# TODO: compare headers from deprecated folders
# TODO: create an .bt3ignore parser
# TODO: change back end, remote storage
# TODO: named branches
# TODO: front end
# TODO: /home/

"""
    Here we just call all the methods for the version control.
"""


def delete_project(backup_dir):
    system_operations.removing_dir_tree(backup_dir)
    system_operations.removing_file(CONFIG_FILE)
    print("Project removed.")


def make_checkout(work_dir, backup_dir, arg1):
    checkout.main(backup_dir, work_dir, arg1)


def log(backup_dir):
    metadata.print_log(backup_dir)


def current(backup_dir):
    metadata.print_latest_snapshot(backup_dir)


def make_snapshot(work_dir, backup_dir, message=""):
    snapshot.main(work_dir, backup_dir, message)


def diff(backup_dir, ss1, ss2):

    try:
        assert(int(ss1)> 0)
        assert(int(ss2)> 0)
    except:
        print("Snapshot values are not valid.")
        default_arg()

    path = backup_dir + '/' + ss1
    try:
        assert(os.path.exists(path))
    except:
        print("Snapshot %s is not valid." %ss1)
        default_arg()

    path = backup_dir + '/' + ss2
    try:
        assert(os.path.exists(path))
    except:
        print("Snapshot %s is not valid." %ss2)
        default_arg()

    metadata.print_diff(backup_dir, ss1, ss2)



"""
    Defining where to place the version control (.b3g)
"""
def first_configuration(arg1):

    if not arg1:
        arg1 = input("Location of the project (myproject): ")
        if arg1 == "" or not os.path.exists(arg1) or arg1 == "." or arg1 == "..":
            print("This location is not valid. Setting project at './workplace' folder.")
            arg1 = 'workplace'

    system_operations.creating_dir_tree(workplace)
    system_operations.creating_file(CONFIG_FILE)
    system_operations.writing_file(CONFIG_FILE, 'w', arg1)

    return arg1


def define_work_folders(arg1):
    arg1 = arg1 or ""

    # if this is the first time or if there is an argument for location
    if arg1 or not os.path.isfile(CONFIG_FILE):
        work_dir = first_configuration(arg1)

    # else get the saved information
    else:
        try:
            with open(CONFIG_FILE) as f:
                config = f.readlines()
                work_dir = config[0].split("\n")[0]
        except:
            print("The work directory is invalid.")
            default_arg()

    return work_dir


def first_configuration(arg1):

    if not arg1:
        arg1 = raw_input("Location of the project (myproject): ")
        if arg1 == "":
            arg1 = '.'

    if not os.path.exists(arg1):
        print("There is no such location. Setting project at the current folder")
        arg1 = '.'

    system_operations.creating_file(CONFIG_FILE)
    system_operations.writing_file(CONFIG_FILE, 'w', arg1)

    return arg1


"""
    Make sure the arguments are ok
"""
def cleanse_arguments(arguments):

    try:
        arg1 = arguments[0]
        assert(len(arg1) < 30) #limit size
    except:
        arg1 = ""
        pass

    try:
        arg2 = arguments[1]
        assert(len(arg2) < 3) #limit size of snapshots
    except:
        arg2 = ""
        pass

    return arg1, arg2




"""
    In case of nothing else working...
"""
def default_arg():
    print("\nExiting...")
    sys.exit(0)





"""
    Main function: Menu, and cleaning.
"""
def main():

    arguments =  system_operations.parsing_cl_argument()
    try:
        option_input = arguments[0]
    except:
        print("You need to give an argument.")
        default_arg()

    arg1, arg2 = cleanse_arguments(arguments[1:])

    work_dir = define_work_folders()
    backup_dir = work_dir + "/" + BACKUP_DIR

    options =  [["snapshot", 'make_snapshot(work_dir, backup_dir, arg1)'], \
                ["ss",  'make_snapshot(work_dir, backup_dir, arg1)'], \
                ["checkout",  'make_checkout(work_dir, backup_dir, arg1)'], \
                ["co",   'make_checkout(work_dir, backup_dir, arg1)'], \
                ["log",  'log(backup_dir)'], \
                ["diff", 'diff(backup_dir, arg1, arg2)'],\
                ["config", "define_work_folders(arg1)"],\
                ['current', "current(backup_dir)"],\
                ['rm', 'delete_project(backup_dir)'],\
                ['default', "default_arg()"]]

    for o in options:
        if option_input == o[0]:
            exec(o[1])

    default_arg()



if __name__ == '__main__':

    main()