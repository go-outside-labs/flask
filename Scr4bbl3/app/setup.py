__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__ = "Set the game."

import pickle
import collections
from config import SCORES, LETTERS, WORDSFILE, WORDSDICT


""" Create dictionary of points"""
def create_dict():

    wordPoints = collections.defaultdict(str)

    with open(WORDSFILE, 'r') as f:

        for word in f:

            word = word.lower().strip()
            points = 0

            for c in word:
                points += SCORES[c]

            wordPoints[word] = points

    with open(WORDSDICT, 'w') as f:

        pickle.dump(wordPoints, f)





""" Create list of letters to be drawn """
def create_list_letters():

    lettersGame = ''

    for letter, freq in LETTERS.items():

        for i in range(freq):
            lettersGame += letter

    return lettersGame




""" Load a pre-existent dictionary"""
def load_dict():

    with open(WORDSDICT, 'r') as f:

        return pickle.load(f)
