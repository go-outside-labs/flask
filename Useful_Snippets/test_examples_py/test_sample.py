#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"




def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

if __name__ == '__main__':
    test_answer()

