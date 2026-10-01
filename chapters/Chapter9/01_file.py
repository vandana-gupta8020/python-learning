# file I/O

#   CHAPTER 9 - FILE I/O
"""
The random-access memory is volatile, and all its contents are lost once a program terminates in order to persist the data forever, we use files.
A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.

Programmer:- computer program written in python   ------------> Write ------------> File
                                                  <------------ read <------------- File

                                         RAM = Volatile (Load program temporaily)
                                         HDD = Non Volatile (Load Program permanent)
"""

# TYPE OF FILES.
"""
There are 2 types of files:
1. Text files (.txt, .c etc)
2. Binary files (.jpg, .dat, etc)
- Python has a lot of functions for reading, updating, and deleting files.


=> OPENING A FILE
Python has an open () function for opening files. It takes 2 parameters: filename and mode.
"""

# open the file in read mode
f = open("file.txt", )
# f = open("file.txt", "r")            # Here, in Read mode, doesn't need mention "r", Because by default it given as openTextManager.

# Read its contents
data = f.read()
# Print its contents
print(data)
# close the file
f.close()