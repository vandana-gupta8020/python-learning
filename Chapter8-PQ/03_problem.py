# 3. How do you prevent a python print() function to print a new line at the end.

print("a")
print("b")
print("c", end="")
print("d", end="")
print("e", end="")

"""Output:-
a
b
cde  
"""


# Explaination:-
""""
- By default, Python's print() function ends with a newline character (\n).
- To prevent it from printing a new line, we can use the 'end' argument. Here, end=" " is a keyword argument.
- It tells print() to end the output with a space instead of a newline."""

print("Hello", end=" ")
print("World!")  # Hello World!  Note:- Here, instead of printing on two lines, it prints on the same line with a space between the words.