#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__ = "Custom test class to test system_operations.py"



import os

import system_operations

from constants import *



class TestClass:

    def test_bootstrap(self):
        system_operations.writing_file(SOURCE, 'a', "This is a test file!")

    def test_one(self):
        system_operations.copying_file(SOURCE, FILE_TO_COPY)
        assert(os.path.isfile(FILE_TO_COPY))


    def test_two(self):
        MESSAGE = "AAAAAAAAAAAAAAAAAAAAAAA"
        SIZE_ADDED = len(MESSAGE) + 1
        SIZE_FILE_BEFORE = os.stat(FILE_TO_WRITE).st_size
        att = 'a'
        system_operations.writing_file(FILE_TO_WRITE, att, MESSAGE)
        SIZE_FILE_AFTER = os.stat(FILE_TO_WRITE).st_size
        assert(SIZE_FILE_BEFORE + SIZE_ADDED == SIZE_FILE_AFTER)


    def test_three(self):
        system_operations.renaming_file(FILE_TO_COPY, FILE_TO_RENAME)
        assert(os.path.isfile(FILE_TO_RENAME) == True)
        assert(os.path.isfile(FILE_TO_COPY) == False)


    def test_four(self):
        system_operations.creating_file(FILE_TO_CREATE)
        assert(os.path.isfile(FILE_TO_CREATE) == True)


    def test_five(self):
        system_operations.removing_file(FILE_TO_DELETE)
        assert(os.path.isfile(FILE_TO_DELETE) == False)


    def test_six(self):
        system_operations.creating_dir_tree(DIR_TO_CREATE)
        assert(os.path.exists(DIR_TO_CREATE))


    def test_seven(self):
        system_operations.removing_dir_tree(DIR_TO_DELETE)
        assert(os.path.exists(DIR_TO_DELETE) == False)


    def test_eight(self):
        system_operations.finding_diffs(FILE_TO_COMPARE1, FILE_TO_COMPARE2, DIFF_FILE)
        assert(os.path.isfile(DIFF_FILE))


    def test_nine(self):
        system_operations.compressing_file(FILE_TO_COMPRESS)
        assert(os.path.isfile(FILE_TO_COMPRESS))


    def test_ten(self):
        file_decompressed = system_operations.decompressing_file(FILE_TO_DECOMPRESS)
        assert(os.path.isfile(file_decompressed))


    def test_eleven(self):
        system_operations.parsing_cl_argument()


    def test_cleaning_up(self):
        system_operations.removing_file(FILE_TO_DECOMPRESS)
        system_operations.removing_file(FILE_TO_RENAME)
        system_operations.removing_file(DIFF_FILE)
        system_operations.removing_file(SOURCE)



if __name__ == '__main__':
    print("$ py.test -q test_class.py")

    """ In case we need pdb to debug
        run with
        $ python -i test_class.py
    import pdb
    tclass = TestClass()

    pdb.set_trace()
    tclass.test_ten()

    """


