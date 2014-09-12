 b3g PhoneBook Manager
=======================

You can use this software in the **command line** or as a **web app**.

Command Line Phone Book
------------------------

A command line tool that manages phone books.


#### Admin Commands

```
# Create a new database or upgrade it:
$ ./phonebook.py db upgrade

# Backup database (migration)
$ ./phonebook.py db migrate

# tests
$ ./phonebook.py tests

```


#### User Commands

```
# Create an entry <name> with <number>
$ ./phonebook.py add <name> <number>

# Change a entry <number>
$ ./phonebook.py change <name> <number>

# Delete an entry
$ ./phonebook.py remove <name>

# Lookup names matching <number>
$ ./phonebook.py find -n <number>

# lookup numbers matching <name>
$ ./phonebook.py find <name>

# help/usage
$ ./phonebook.py help
```



A PhoneBook Web App
---------------------

#### To Install and Use

```
# Get the dependences
$ pip install -r requirements.txt

# Running at localhost:5000
$ python manage runserver
```









Aux Functions (preparation):
-----------------------------
- parsing command-line arguments
- data structures that allow fast lookup (hash tables)
- looking through strings for matches
- using a database
- doing http requests of a server your server




To Do
------
- allow search by partial name - not just beginning of name
- case insensitive search
- make names work without using quotes
- How long does it take to add or lookup 10,000 names and numbers? What's the bottleneck? 1,000,000?
- Add tab completion






