#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' using iterator enumerate to create a grep command '''


import sys

def grep_word_from_files():
    word = sys.argv[1]
    for filename in sys.argv[2:]:
        with open(filename) as file:
            for lino, line in enumerate(file, start=1):
                if word in line:
                    print("{0}:{1}:{2:.40}".format(filename, lino, line.rstrip()))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: grep_word_from_files.py word infile1 [infile2...]")
        sys.exit()
    else:
        grep_word_from_files()




