# 10. Write a program to wipe out the content of a file using python.



# First, open the file in read mode to get the content
with open("this_copy.txt", "w") as f:
    f.write("")        # wipe out the content of file "this_copy.txt"