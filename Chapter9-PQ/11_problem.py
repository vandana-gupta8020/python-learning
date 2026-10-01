# 11. Write a python program to rename a file to "renamed_by_python.txt".



# First, open the file in read mode to get the content
with open("11_old.txt") as f:
    content = f.read()        # Read the file content as a string
    

with open("renamed_by_python.txt", "w") as f:
    f.write(content)          # Read the file content as a string


