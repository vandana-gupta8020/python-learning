# Ques4:- Label of the program written in problem 4 with comments.

import os

# Specify the directory you want to list (make sure this folder exists)
directory_path = 'C:\\Users\\CE00161624\\Desktop'

# List all files and directories in the specified path
try:
    contents = os.listdir(directory_path)

    # Print each file and directory name
    for item in contents:  # Fixed indentation
        print(item)

except FileNotFoundError as e:
    print(f"Error: {e}")

"""
COMMENTS: Comments are used to write something which the programmer does not want to execute. This can be used to mark author name, date etc.

Types of comments:-
Ther are two types of comments in python.
"""