#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__ = "A Scrabble online game."


import os.path
import sys
from setup import load_dict, create_dict, create_list_letters
from turn import generate_combination
from config import WORDSDICT



def main():

    """ Load configurations for the game """

    # create and load dictionary of points
    if not os.path.isfile(WORDSDICT):
        print "Generating dictionary..."
        create_dict()


    try:
        wordPoints = load_dict()

    except:
        print ("Could not load the dictionary.")
        sys.exit()



    ''' get the list '''
    letters = raw_input("Type the letters: ")
    if len(letters) > 15:
        return "Hand should be at most 15 letters."
    handCombination = generate_combination(letters)


    """ show sorterd, with point """
    valid = []
    for comb in handCombination:
        if comb in wordPoints.keys():
            valid.append([comb, wordPoints[comb]])


    print "Possible words are:"
    for w in sorted(valid, reverse=True):
        print w[0] + " - Points: " + str(w[1])





if __name__ == '__main__':
    main()
