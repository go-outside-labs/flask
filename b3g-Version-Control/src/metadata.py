#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__= "Builds the metadata for our version control."


import datetime
import sys
import os

import system_operations
from constants import BACKUP_DIR, CONTEND_DIR, OLD_VERSIONS_DIR




"""
    print the HEAD file
"""
def print_log(dest):

    header_file = dest + '/HEAD'
    try:
        assert(os.path.isfile(header_file))
    except:
        print("HEAD is not defined yet. Try to create a snapshot first.")
        sys.exit(0)

    with open(header_file, 'r') as f:
        for line in f:
            print(line.split("\n")[0])



"""
    print the current snapshot
"""
def print_latest_snapshot(dest):

    # Verify whether destination folder(.b3g) exists
    if not os.path.exists(dest):
        print("You do not have any snapshot yet.")
        sys.exit(0)

    folders = system_operations.create_list_of_folders(dest)
    folders = map(int, folders)

    print("The current snapshot is " + str(max(folders)) + '.\n')




"""
    print the difference between two snapshots
"""
def print_pretty_header(dest, ss1, ss2):

    header_file = dest + '/HEAD'
    with open(header_file, 'r') as f:
        for line in f:
            number = line.split(':')
            if number[0] == ss1 or number[0] == ss2:
                message = number[1].split(",")
                print("Snapshot %s was created on %s" %(number[0], message[0]))
                print("Snapshot message: " + message[1])




def print_pretty(diff_snapshot1, diff_snapshot2, ss1, ss2):

    print("Printing the differences between snapshots {0} and {1}:". format(ss1,ss2))
    print("Diff in snaphost %s:" %ss1)
    for file in diff_snapshot1:
        print(file)
    print("Diff in snaphost %s:" %ss2)
    for file in diff_snapshot2:
        print(file)


def print_diff(dest, ss1, ss2):

    # create two sets with files from the two snapshots
    snapshot1 = set(system_operations.create_list_of_files(dest + "/" + ss1))
    snapshot2 = set(system_operations.create_list_of_files(dest + "/" + ss2))

    # get all the files that are not in common
    diff_snapshot1 = snapshot1 - snapshot2
    diff_snapshot2 =  snapshot2 - snapshot1

    # print diff
    print_pretty_header(dest, ss1, ss2)
    print_pretty(diff_snapshot1, diff_snapshot2, ss1, ss2)

    return diff_snapshot1, diff_snapshot2



"""
    update the header and is called in the checkout
"""
def update_header_checkout(source, argument, folder_id):

    # move the old header to the folder id
    deprecated_head = source + "/" + OLD_VERSIONS_DIR + "/HEAD_" + folder_id
    head_file = source + '/HEAD'
    old_head = system_operations.renaming_file(head_file, deprecated_head)

    # copy anything before the snapshot to the new header
    new_lines = []
    with open(deprecated_head) as f:
        lines = f.readlines()
        for line in lines:
            if line.split(":")[0] != argument:
                new_lines.append(line.split("\n")[0])
            else:
                break

    # write the new HEAD file
    system_operations.creating_file(head_file, 'w')

    with open(head_file) as f:
        for line in new_lines:
            system_operations.writing_file(head_file, 'a', line)

    update_header_snapshot(argument, source, "# checkout at " + folder_id)




"""
    update the header and is called in the snapshot
"""
def update_header_snapshot(latest_snapshot_number='0', dest=BACKUP_DIR, message=""):

    # check if there is a head file, otherwise, create one
    header_file = dest + '/HEAD'
    system_operations.creating_file(header_file)

    # write the header number
    now = datetime.datetime.now()
    snapshot_info = latest_snapshot_number + ': ' + now.strftime("%Y/%m/%d-%Hh%Mm") \
                + ', ' + message
    system_operations.writing_file(header_file, 'a', snapshot_info)





if __name__ == '__main__':

    print("\n--------------------------------------------------------------")
    print("This is just a module. To run the full program, please type:")
    print("$ ./b3g OPTIONS")
    print("--------------------------------------------------------------\n")
