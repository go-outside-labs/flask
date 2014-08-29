#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


# content of test_class.py
# $ py.test -q test_class.py

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')




if __name__ == '__main__':
    print("$ py.test -q test_class.py")


