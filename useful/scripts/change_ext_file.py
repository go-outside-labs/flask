#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

""" read a file and an extension from the command line and produces a copy with its extension changed"""


import os
import sys
import shutil

def change_file_ext():
    if len(sys.argv) < 2:
        print("Usage: change_ext.py filename.old_ext 'new_ext'")
        sys.exit()

    name = os.path.splitext(sys.argv[1])[0] + "." + sys.argv[2]
    print (name)

    try:
        shutil.copyfile(sys.argv[1], name)
    except OSError as err:
        print (err)



if __name__ == '__main__':
    change_file_ext()


