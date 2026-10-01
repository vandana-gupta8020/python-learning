# 1. Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

# opens the file in read mode "r"
f = open("poems.txt", "r")
data = f.read()     # reads the file
if("twinkle" in data):
    print("The word 'twinkle' is present in the data.")
else:
    print("The word 'twinkle' is not present in the data.")



f.close()           # close the file