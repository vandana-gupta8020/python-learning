# 9. Write a program to find out whether a file is identical & matches the content of another file.

# First, open the file in read mode to match the content
with open("this.txt") as f:
    content1 = f.read()        # Read the file content as a string

  
# open the file in read mode to match the content
with open("this_copy.txt") as f:
    content2 = f.read()        # Read the file content as a string
    
if(content1 == content2):        # comparing their contents
    print("Yes! Both files are indentical")
    
else:
    print("No! Bothe files are not indentical")   