__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__ = "Define a scrabble game turn."


import random
import string
import collections
import itertools

from config import LETTERS


"""
    General methods for the players
"""

def generate_hand(lettersGame, numberOfPiecesHand, lettersDict):
    count = 0
    lettersHere = ""
    while count < numberOfPiecesHand:
        l = random.choice(lettersGame)
        if lettersDict[l] > 0:
            lettersDict[l] -= 1
            lettersHere += l.lower()
            count += 1

    return lettersHere, lettersDict



def generate_combination(lettersHere):
    handCombination = []

    for i in range(1, len(lettersHere)+1):
        item = list(itertools.permutations(lettersHere, i))
        for j in item:
            word = ""
            for k in j:
                word += k
            handCombination.append(word)

    #print handCombination
    return handCombination




def generate_points_combination(wordPoints, handCombination):
    points = 0
    word = ""
    for comb in handCombination:
        if comb in wordPoints.keys() and wordPoints[comb] > points:
            points = wordPoints[comb]
            word = comb
    return points, word




def get_letters_left(word, lettersHere):
    i, j = 0, 0
    while i < len(word) and  j < len(lettersHere):
        if word[i] == lettersHere[j]:
            lettersHere = lettersHere[:j] + lettersHere[j+1:]
            i += 1
            j = 0
        else:
            j += 1

    return lettersHere



"""
    Computer's Game
"""


def computerTurn(wordPoints, lettersGame, numberOfPiecesHand, lettersDict, letters):

    # get the best combination for points
    lettersHere, lettersDict = generate_hand(lettersGame, numberOfPiecesHand, lettersDict)
    lettersHere += letters

    # get best word
    handCombination = generate_combination(lettersHere)
    points, word = generate_points_combination(wordPoints, handCombination)

    # subtract the word from hand
    lettersHere = get_letters_left(word, lettersHere)

    return points, word, lettersHere, lettersDict



"""
    Humans's Game
"""
def humanTurn(wordPoints, lettersGame, numberOfPiecesHand, lettersDict, letters):

   # get the best combination for points
    lettersHere, lettersDict = generate_hand(lettersGame, numberOfPiecesHand, lettersDict)
    lettersHere += letters

    # get best word
    handCombination = generate_combination(lettersHere)

    print "\nYour hand is:"
    print lettersHere

    turnDone = False
    points = 0
    word = ""
    count = 0
    while not turnDone:
        word = raw_input("What's the word? ")
        count += 1
        if word in wordPoints.keys():
            points = wordPoints[word]
            turnDone = True
        elif count > 10:
            turnDone = True
            print " I guess you don't know how to play... You lost your turn."






    # subtract the word from hand
    lettersHere = get_letters_left(word, lettersHere)

    return points, word, lettersHere, lettersDict


