#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__= "Simple system operation functions."


""" Disclaimer: if you're not bothered about portability: os.system approach
    (this simply call the underlying OS command line)
    if you want portability: shutil method (uses Python-only code) """


import shutil
import os
import filecmp
import gzip
import sys

from constants import *


'''
    Here we simply write the text into a file.
    Similar to "echo MESSAGE >> FILENAME
'''
def writing_file(FILENAME, att='a', MESSAGE=""):

    try:
        with open(FILENAME, att) as f:
            f.write(MESSAGE)
            f.write('\n')

    except IOError as e:
        print "I/O error({0}): {1} for file {2}".format(e.errno, e.strerror, FILENAME)




'''
    Here we copy the contents of a file to another file.
    Similar to "cp" in linux.
'''
def copying_file(SOURCE, DESTINATION):

    try:
        shutil.copy(SOURCE, DESTINATION)
        # could also use
        # os.system ("copy %s %s" % (filename1, filename2))
        # also, for recursively copy a tree
        # shutil.copytree(src, dest)

    # source and destination are the same file
    except shutil.Error as e:
        print("Error: %s" % e)

    # source does not exist
    except IOError as e:
        print "I/O error({0}): {1} for file {2}".format(e.errno, e.strerror, SOURCE)


def moving_dir(SOURCE, DESTINATION):

    try:
        shutil.move(SOURCE, DESTINATION)

    # source and destination are the same file
    except shutil.Error as e:
        print("Error: %s" % e)

    # source does not exist
    except IOError as e:
        print "I/O error({0}): {1} for file {2}".format(e.errno, e.strerror, SOURCE)






'''
    Here we rename/move a file.
    Similar to  "mv" in linux.
'''
def renaming_file(SOURCE, DESTINATION):

    try:
        shutil.move(SOURCE, DESTINATION)

    # source and destination are the same file
    except shutil.Error as e:
        print("Error: %s" % e)

    # source does not exist
    except IOError as e:
        print "I/O error({0}): {1} for file {2}".format(e.errno, e.strerror, SOURCE)




'''
    Here we create an empty new file.
    Similar 'touch' in linux.
'''
def creating_file(FILENAME, att='a'):

    try:
        f = open(FILENAME, att)
        f.close()

    except IOError as e:
        print "I/O error({0}): {1} for file {2}".format(e.errno, e.strerror, FILENAME)



'''
    Here we remove a file.
    Similar to 'rm' in linux.
'''
def removing_file(FILENAME_TO_DELETE):

    if os.path.isfile(FILENAME_TO_DELETE):
        return os.remove(FILENAME_TO_DELETE)

    else:
        print("Error: %s file not found." % FILENAME_TO_DELETE)



'''
    Here we create a new directory.
    Similar to 'mkdir' in linux.
'''
def creating_dir_tree(DIR_TO_CREATE):

    if not os.path.exists(DIR_TO_CREATE):
        os.makedirs(DIR_TO_CREATE)



'''
    Here we remove the entire directory tree.
    Similar to 'rm -rf' in linux.
'''
def removing_dir_tree(DIR_TO_DELETE):

    try:
        # we could also use
        shutil.rmtree(DIR_TO_DELETE)
        #os.rmdir(DIR_TO_DELETE)
    except OSError, e:
        print ("Error: %s - %s." % (e.filename,e.strerror))




'''
    Here we want to find the difference between two files
    and save into difference log file.
    We use two aux functions to print.
'''
def print_lines(FILENAME):

    try:
        with open(FILENAME, 'r') as f:
            lines = f.readlines()
            print("---------- %s ----------" %FILENAME)
            for line in lines:
                print(line.strip('\n'))
            print(" ")

    except IOError as e:
        print "I/O error({0}): {1} for file {2}".format(e.errno, e.strerror, FILENAME)

    return lines


def print_diff_results(diff, DIFF_FILE):

    print ("---------- diff ----------")

    for line in diff:
        print(line.strip('\n'))

    for line in diff:
        writing_file(DIFF_FILE, 'a', line.strip('\n'))


def finding_diffs(FILE_TO_COMPARE1, FILE_TO_COMPARE2, DIFF_FILE="diff.log"):

    l1 = print_lines(FILE_TO_COMPARE1)
    l2 = print_lines(FILE_TO_COMPARE2)

    diff = []
    lbigger = max(l1,l2)
    lsmaller = min(l1,l2)

    for i, line in enumerate(lsmaller):
        if line != lbigger[i]:
            diff.append(line)

    diff.extend(lbigger[i+1:])

    print_diff_results(diff, DIFF_FILE)




'''
    Here we write methods to compress/ uncompress files.
'''
def compressing_file(FILE_TO_COMPRESS):

    try:
        f_in = open(FILE_TO_COMPRESS)
        f_out = gzip.open(FILE_TO_COMPRESS + '.gz', 'wb')
        f_out.writelines(f_in)
        f_in.close()
        f_out.close()

    except IOError as e:
        print "I/O error({0}): {1} for file {2}".format(e.errno, e.strerror, FILE_TO_COMPRESS)


def decompressing_file(FILE_TO_DECOMPRESS):

    try:
        f_in = gzip.open(FILE_TO_DECOMPRESS, 'rb')
        contend = f_in.read()
        f_in.close()

        file_dec = FILE_TO_DECOMPRESS.split('.')[0] + '.txt'
        f_out = open(file_dec, 'w')
        f_out.writelines(contend)
        f_out.close()

        return file_dec

    except IOError as e:
        print "I/O error({0}): {1} for file {2}".format(e.errno, e.strerror, FILE_TO_DECOMPRESS)



'''
    Here justing showing how to parse arguments, might be useful later
'''
def parsing_cl_argument():

    arguments = sys.argv[1:]
    return arguments



'''
    Here we do some manipulations on the folders/dir
'''
def create_list_of_files(DIR):

    files = [f for f in os.listdir(DIR) if os.path.isfile(DIR + '/' + f)]
    return files


def create_list_of_folders(DIR):

    folders = [f for f in os.listdir(DIR) if os.path.isdir(os.path.join(DIR, f))]
    return folders







if __name__ == '__main__':

    print("\n--------------------------------------------------------------")
    print("This is just a module. To run the full program, please type:")
    print("$ ./b3g OPTIONS")
    print("--------------------------------------------------------------\n")


    print("     The system command available are: \n")
    print("1 -  writing_file(FILENAME, att, MESSAGE)")
    print("2 -  copying_file(SOURCE, DESTINATION)")
    print("3 -  Renaming_file(SOURCE, DESTINATION)")
    print("4 -  creating_file(FILENAME)")
    print("5 -  removing_file(FILENAME_TO_DELETE)")
    print('6 -  creating_dir_tree(DIR_TO_CREATE)')
    print("7 -  removing_dir_tree(DIR_TO_DELETE)")
    print("8 -  finding_diffs(FILE_TO_COMPARE1, FILE_TO_COMPARE2, DIFF_FILE)")
    print("9 -  compressing_file(FILE_TO_COMPRESS)")
    print("10 - decompressing_file(FILE_TO_DECOMPRESS)")
    print("11 - parsing_cl_argument()")
    print("12 - create_list_of_files(DIR)")
    print("13 - create_list_of_folders(DIR)")
    print("\n")
