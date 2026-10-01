

"""
=> OTHER METHODS TO READ THE FILE.
   - We can also use f.readline() function to read one full line at a time.
f.readline()     # Read one line from the file.


=> MODES OF OPENING A FILE:-
->  'r' open for reading
->  'w' open for writing
->  'a' open for appending
->  '+' open for updating.
->  'rb' will open for read in binary mode.
->  'rt' will open for read in text mode.


=> WRITE FILES IN PYTHON
In order to write to a file, we first open it in write or append mode after which, we use the python's f.write() method to write to the filel

"""

# pass the text/string what you want to write in the file.
str = "The random-access memory(RAM) is 'volatile'."
# opens the new file using write mode
f = open("myfile_write.txt", "a")
# writes the text which is passed in string in the myfile_write.txt file.
f.write(str)
# close the file
f.close()