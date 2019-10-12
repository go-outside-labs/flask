#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__ = "A Scrabble online game."



import os.path
from setup import load_dict, create_dict, create_list_letters
from turn import computerTurn, humanTurn
from view import goodbye, greetings, printStatus
from config import WORDSFILE, WORDSDICT, LETTERS



def main():

    greetings()

    """ Load configurations for the game """

    # create and load dictionary of points
    if not os.path.isfile(WORDSDICT):
        create_dict()

    try:
        wordPoints = load_dict()
    except:
        return "Could not load the dictionary."

    try:
        lettersGame = create_list_letters()
    except:
        return "Could not create list of letters."



    """ set game variables """
    piecesLeft = len(lettersGame)
    numberOfPiecesHand = 5
    lettersDict = LETTERS

    lettersPC = ""
    pointsPC = 0
    wordsPC = []

    lettersHuman = ""
    pointsHuman = 0
    wordsHuman = []


    """ Game Loop """
    while piecesLeft >= 2*numberOfPiecesHand:

        # computer's turn
        print("\n--> Computer's Turn:")
        points, word, lettersPC, lettersDict =  computerTurn(wordPoints, lettersGame, \
                            numberOfPiecesHand, lettersDict, lettersPC)

        pointsPC += points
        wordsPC.append(word)
        printStatus(word, str(points), str(pointsPC))




        # human's turn
        print("\n--> Your Turn:")
        points, word, lettersHuman, lettersDict =  humanTurn(wordPoints, lettersGame, \
                            numberOfPiecesHand, lettersDict, lettersHuman)

        pointsHuman += points
        wordsHuman.append(word)
        printStatus(word, str(points), str(pointsHuman))


        break

    """ Game Finalization """
    goodbye(str(pointsHuman), str(pointsPC), wordsHuman, wordsPC)




if __name__ == '__main__':
    main()
