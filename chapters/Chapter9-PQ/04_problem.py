# 4. A file contains a word "donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file.


word = "donkey"
# First, open the file in read mode to get the content
with open("04_file.txt", "r") as f:
    content = f.read()      # Read the file content as a string
    
    newContent = content.replace(word, "#####")      # Replace all occurrences of "donkey" with "#####"
    
# Now write the updated content back to the same file
with open("04_file.txt", "w") as f:
    newContent = f.write(newContent)
    
    f.close()