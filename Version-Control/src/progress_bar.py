#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__= "Simple progress bar class, modified from http://www.pythoncentral.io"



import sys
import time


class ProgressBar(object):

    def __init__(self, message, width=20):

        self.width = width
        self.message = message
        self.progressSymbol = u'\u25A0'
        self.emptySymbol = u'\u25A1'

        if self.width < 0:
            self.width = 0


    def update_bar(self, progress):

        totalBlocks = self.width
        filledBlocks = int(round(progress / (100 / float(totalBlocks)) ))
        emptyBlocks = totalBlocks - filledBlocks

        progressBar = self.progressSymbol * filledBlocks + \
                      self.emptySymbol * emptyBlocks

        if not self.message:
            self.message = u''

        progressMessage = u'\r{0} {1}  {2}%'.format(self.message,
                                                    progressBar,
                                                    progress)

        sys.stdout.write(progressMessage)
        sys.stdout.flush()



    def calculateAndUpdate(self, done, total):

        progress = int(round( (done / float(total)) * 100) )
        self.update_bar(progress)





if __name__ == '__main__':

    print("\n--------------------------------------------------------------")
    print("This is just a module. To run the full program, please type:")
    print("$ ./b3g OPTIONS")
    print("--------------------------------------------------------------\n")

    print("Testing progress bar...")
    pb = ProgressBar(message)

    for i in range(1, 10):
        pb.calculateAndUpdate(i, 9)
        time.sleep(0.1)

    print(" ")

