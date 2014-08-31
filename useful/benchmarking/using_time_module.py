#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' a simple example of timing a function '''



import time

def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i

    end = time.time()

    return theSum,end-start



if __name__ == '__main__':
    n = 5
    print("Sum is %d and required %10.7f seconds"%sumOfN2(n))
    n = 200
    print("Sum is %d and required %10.7f seconds"%sumOfN2(n))

