# WITH STATEMENT
"""
The best way to open and close the file automatically is the 'with' statement."""

# Open the file in read mode using 'with', which automatically closes the file
# with open("identify_function.md", "r") as f:     # WARNING: Ensure "identify_function.md" exists in the same directory, or this will raise a FileNotFoundError.

with open("identify_function.md", "r", encoding="utf-8") as f:    # Open the file in read mode using 'with' and utf-8 encoding.
# NOTE: Using encoding="utf-8" to handle special/non-English characters and avoid decode errors across all systems. Example: 😊, हिंदी, 中文 – all are supported.
  text = f.read()       # Read the contents of the file

print(text)             # Print the contents


f = open("file.txt")
print(f.read())
f.close()
# The same can be written using 'with' statement like this:


# 🔁 Method: Using with and for Loop

with open("file.txt") as f:
        print(f.read())
# we don't have to explicitly close the file.       # ` f.close() `