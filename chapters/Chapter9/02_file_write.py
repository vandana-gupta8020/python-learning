# for writing file :-


# pass the text/string what you want to write in the file.
str = "The random-access memory(RAM) is 'volatile'."
# opens the new file using write mode
f = open("myfile_write.txt", "w")
# writes the text which is passed in string in the myfile_write.txt file.
f.write(str)
# close the file
f.close()