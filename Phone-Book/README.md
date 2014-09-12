 b3g PhoneBook Manager
=======================

You can use this software in the command line or as a web app.


Command Line Phone Book
------------------------

A command line tool that manages phone books.

It uses ```pickle``` to save a Python dictionary (lookup O(1)).


#### Admin Commands

```
# Create a new database:
$ ./phonebook.py create

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
$ ./phonebook.py find_num <number>

# lookup numbers matching <name>
$ ./phonebook.py find <name>
```

#### Example

```
$ ./phonebook.py create
New PhoneBook created.
$ ./phonebook.py add darth 44444
New entry added.
$ ./phonebook.py add matt 9342345356
New entry added.
$ ./phonebook.py find darth
Phone for darth is 44444
$ ./phonebook.py find vader
Name not found.
$ ./phonebook.py find_num 44444
Name for 44444 is darth
$ ./phonebook.py change darth 11111
darth entry changed to 11111
$ ./phonebook.py find_num 44444
Phone not found.
$ ./phonebook.py find darth
Phone for darth is 11111
$ ./phonebook.py remove darth
darth deleted
$ ./phonebook.py find darth
Name not found.
$  ./phonebook.py find_num 11111
Phone not found.
```


