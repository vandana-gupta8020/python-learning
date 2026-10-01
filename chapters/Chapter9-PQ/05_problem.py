# 5. Repeat program 4 for a list of such words to be censored.

"""
problem 4:- 
- A file contains the word "donkey" multiple times.
- Program replaces "donkey" with "#####" in the same file.
"""
# list of censored words
censored_words = ["donkey", "idiot", "stupid", "fool"]

# Read the file content
with open("04_file.txt", "r") as f:
    content = f.read()

# Replace each censored word in the content
for word in censored_words:
    content = content.replace(word, "#" * len(word))  # update the content itself

# Write the updated content back to the file
with open("04_file.txt", "w") as f:
    f.write(content)
   
    f.close()


