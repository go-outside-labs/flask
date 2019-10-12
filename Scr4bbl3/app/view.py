#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__ = "The view."



def goodbye(pointsUser, pointsPC, wordsUser, wordsPC):

    print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "                  GAME OVER"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print

    if pointsUser > pointsPC:
        print "You won with " + pointsUser + " points."
        print "The computer lost with " + pointsPC + " points."
    elif pointsUser < pointsPC:
         print "You lost with " + pointsUser + " points."
         print "The computer won with " + pointsPC + " points."
    else:
        print "Everybody wins with " + pointsPC + " points."

    print
    print "Your words were: "
    for w in wordsUser:
        print w
    print
    print "The computer's words were: "
    for w in wordsPC:
        print w



def greetings():

    print
    print " ~~~~~~~~~~~~ Welcome to Scr4bb3! ~~~~~~~~~~~~"
    print
    print " Game is starting... "
    print



def printStatus(word, points, total):

    print
    print "Word: " + word + ", with " + points + " points. SCORE: " + total + '.'
