# 8. Write a program to make a copy of a text file "this.txt"


# First, open the file in read mode to get the content
with open("this.txt") as f:
    content = f.read()        # Read the file content as a string

# In write mode, make the copy of a text file "this.txt"    
with open("this_copy.txt", "w") as f:
    content = f.write(content)       # write the file content in the text file "this_copy.txt"
    
f.close()           # close the file