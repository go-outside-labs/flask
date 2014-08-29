#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__ = "Custom test class to test the program setup"



import os

import snapshot, metadata, checkout, b3g, system_operations
from constants import BACKUP_DIR, CONTEND_DIR, CONFIG_FILE





class TestClass:

    def test_settingup(self):
        assert(False)
        system_operations.creating_dir_tree(CONTEND_DIR)
        system_operations.creating_file(CONTEND_DIR + "/test.txt" )


    def test_cleaning_up(self):
        assert(False)
        system_operations.removing_dir_tree(BACKUP_DIR)
        system_operations.removing_dir_tree(CONTEND_DIR)
        system_operations.removing_file(CONFIG_FILE)



if __name__ == '__main__':
    print("USAGE: $ py.test -q test_b3g.py")

