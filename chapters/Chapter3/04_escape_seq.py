# ESCAPE SEQUENCE CHARACTERS:-

"""Sequence of characters after backslash "\" - Escape Sequence characters
Escape Sequence characters comprise of more than one character but represent one character when used within the strings.
example \n; \t; \';\\etc.
newline tab singlequote backslash."""

# These are escape sequences, not methods. Escape sequences are special characters used within strings to represent certain whitespace characters or other characters that are difficult to type directly (like a newline \n or a tab \t).


# Here are some commonly used "ESCAPE SEQUENCE CHARACTERS" in Python:
# \n → Newline (Moves to the next line)
# \t → Tab (Inserts a tab space)
# \\ → Backslash (Inserts a \ character)
# \' → Single quote (Inserts ' inside a string)
# \" → Double quote (Inserts " inside a string)
# \r → Carriage return (Moves the cursor to the beginning of the line)
# \b → Backspace (Deletes one character)
# \f → Form feed (Moves to the next page in printing)
# \v → Vertical tab (Inserts vertical spacing)
# \ooo → Octal value (Represents a character in octal format)
# \xhh → Hexadecimal value (Represents a character in hexadecimal format)"""
# ~ → seperater 

# 1️⃣ \n → Newline (Moves to the next line)
# Method: splitlines() (Splits string by newlines)
text = "Hello\nWorld"
print(text.splitlines())  # Output: ['Hello', 'World']

# 2️⃣ \t → Tab (Inserts a tab space)
# Method: expandtabs() (Sets tab size)
text = "Hello\tWorld"
print(text.expandtabs(10))  # Output: 'Hello     World' (Tab space expanded to 10)

# 3️⃣ \\ → Backslash (Inserts a \ character)
# Method: replace() (Replaces backslashes)
text = "C:\\Users\\Name"
print(text.replace("\\", "/"))  # Converts Windows path to Unix format    Output: C:/Users/Name

# 4️⃣ \' → Single quote (Inserts ' inside a string)
# Method: count() (Counts occurrences of ')
text = "It\'s a great day!"
print(text.count("\'"))  # Output: 1 (Counts single quote)

# 5️⃣ \" → Double quote (Inserts " inside a string)
# Method: count() (Counts occurrences of ")
text = "She said, \"Hello!\""
print(text.count("\""))  # Output: 2 (Counts double quotes)

# 6️⃣ \r → Carriage return (Moves the cursor to the beginning of the line)
# Method: replace() (Removes carriage return effect)
text = "Hello\rWorld"
print(text.replace("\r", ""))  # Output: 'World' (Removes carriage return)

# 7️⃣ \b → Backspace (Deletes one character)
# Method: replace() (Removes backspace effect)
text = "Hello\bWorld"
print(text.replace("\b", ""))  # Output: 'HelloWorld' (Backspace removed)

# 8️⃣ \f → Form feed (Moves to the next page in printing)
# Method: replace() (Removes form feed)
text = "Hello\fWorld"
print(text.replace("\f", " "))  # Output: 'Hello World' (Replaces form feed with space)

# 9️⃣ \v → Vertical tab (Inserts vertical spacing)
# Method: replace() (Replaces vertical tab with a space)
text = "Hello\vWorld"
print(text.replace("\v", " "))  # Output: 'Hello World'

# 🔟 \ooo → Octal value (Represents a character in octal format)
# Method: encode().decode() (Converts octal to a string)
text = "\110\145\154\154\157"  # Octal for 'Hello'
print(text.encode().decode())  # Output: 'Hello'

# 1️⃣1️⃣ \xhh → Hexadecimal value (Represents a character in hexadecimal format)
# Method: encode().decode() (Converts hex to a string)
text = "\x48\x65\x6C\x6C\x6F"  # Hex for 'Hello'
print(text.encode().decode())  # Output: 'Hello'


# Escape Sequence Character using in the code:-

a = "She is workaholic but\nunwelthy"
b = "Python is an iterperator\tcode"
c = "Escape sequences are special characters used within \"strings\""
print(a)
print(b)
print(c)

print("Hello", 6, 7, sep= "~", end = "009\t")
print("Hello World!")

x = 5
print(~x)


