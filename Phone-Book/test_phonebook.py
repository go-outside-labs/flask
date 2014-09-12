#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__= "Unittest - CI PhoneBook Manager"


import unittest
import os
import phonebook
dbname_test = 'test_phonebook.pickle'



class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        phonebook.create_db(dbname=dbname_test)
        phonebook.add_entry(values=['Matt', '123'], dbname=dbname_test)

    def tearDown(self):
        if os.path.isfile(dbname_test):
            return os.remove(dbname_test)

    def test_find_name(self):
        self.assertTrue(phonebook.find_name(values=['Matt'], dbname=dbname_test))
        self.assertFalse(phonebook.find_name(values=['Joe'], dbname=dbname_test))

    def test_find_num(self):
        self.assertTrue(phonebook.find_phone(values=['123'], dbname=dbname_test))
        self.assertFalse(phonebook.find_phone(values=['234'], dbname=dbname_test))

    def test_change(self):
        phonebook.change_number(values=['Matt', '3333'], dbname=dbname_test)
        self.assertTrue(phonebook.find_phone(values=['3333'], dbname=dbname_test))


    def test_del(self):
        phonebook.del_entry(values=['Matt'], dbname=dbname_test)
        self.assertFalse(phonebook.find_name(values=['Matt'], dbname=dbname_test))



if __name__ == '__main__':
    unittest.main()
