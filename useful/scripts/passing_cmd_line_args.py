#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


''' print command line arguments '''

import sys


def main():

    for arg in sys.argv[1:]:
        print arg

if __name__ == "__main__":
    main()




