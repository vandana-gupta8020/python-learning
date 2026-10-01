
"""INPUT() FUNCTION
This function allows the user to take input from the keyboard as a string.
A = input("enter name")      >-- if a is "harry", the user entered harry
It is important to note that the output of input is always a string (even is a number is entered)."""


a = input("Enter number 1")

b = input("Enter number 2")

print("Number a is: ", a)
print("Number b is: ", b)


a = input("Enter number 1: ")

b = input("Enter number 2: ")

c = input("Enter number 3: ")

print("Number a is: ", a)
print("Number b is: ", b)
print("Number c is: ", c)
print("Sum is ",  a + b)     # Concatenating two strings



"""In Python, string 'Concatenation' refers to the process of joining two or more strings together to create a single string. This is typically done using the + operator."""
# Concatenating(merge) two strings
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2      # Adding a space between the words
print(result)                         # Output: Hello World  <--Note: "Hello" and "World" are concatenated using the + operator with a space " " in between, resulting in the string "Hello World"-->



a = int(input("Enter number 1: "))

b = int(input("Enter number 2: "))


print("Sum is ", a + b)