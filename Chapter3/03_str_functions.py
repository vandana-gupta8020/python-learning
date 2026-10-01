# What is function in python? 
"""- In Python, functions are blocks of reusable code that perform a specific task. They help in making the code modular, organized, and efficient, so you don't have to write the same logic multiple times. 
'OR'                                                                                                              
Python mein functions ek tarike ka block of code hote hain jo specific task perform karte hain. Ye code reusability ke liye use kiye jate hain, taaki ek baar likha hua code baar-baar use kiya ja sake.

Why Use Functions?
✔ Makes the code organized & readable
✔ Avoids repetition (write once, use multiple times)
✔ Improves maintainability

Types of Functions in Python:
1️⃣ Built-in Functions:- Predefined functions provided by Python (e.g., print(), len(), type()).
2️⃣ User-Defined Functions:- Functions created by the user using the def keyword. For example:-

Python functions are categorized into these five main types, and they help in writing clean, efficient, and reusable code. 🚀
"""

# 1️⃣ Built-in Functions (Predefined by Python) Python has many built-in functions that perform common tasks.
"""print():- Displays output
len():- Returns the length of an object
type():- Returns the type of an object"""

print(len("Python"))  # Output: 6
print(type(10))       # Output: <class 'int'>

# 2️⃣ User-Defined Functions (Created by the user) These functions are defined using the def keyword to perform specific tasks.
def greet(name):
    print("Hello, " + name + "!")

greet("Amit")  # Output: Hello, Amit!

# 3️⃣ Lambda Functions (Anonymous Functions) A small, one-line function that doesn’t have a name. It’s used for short operations.
square = lambda x: x*x
print(square(5))  # Output: 25

# 4️⃣ Recursive Functions (Function calling itself) A function that calls itself to solve a problem in smaller steps.
def factorial(n):       # (Factorial using recursion)
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 5️⃣ Higher-Order Functions (Functions that take another function as an argument)
def apply_twice(func, value):
    return func(func(value))

double = lambda x: x * 2
print(apply_twice(double, 5))  # Output: 20


def greet(name):  
    print("Hello, " + name + "!")  

greet("Amit")        #  Output:- Hello, Amit!


# STRING FUNCTIONS:-
# Some of the mostly used functions to perform operations on or manipulate strings are:
# 1. len () function-This function returns the length of the strings.
name = 'harry'
print(len('harry')) # returns 5

# 2. String.endswith("rry") - This function_tells whether the variable string ends with the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends with rry.
MyString = "harry"
print(MyString.endswith("rry"))         # output: True

# 3. string.count("c")-counts the total number of occurrences of any character.
string = "abracadabra"
count = string.count("c")
print(count)             # Output: 1


# 4. string.capitalize()-This function capitalize the first character of a given string.
s = "hello world"
capitalize_string = s.capitalize()
print(capitalize_string)              # output: "Hello world"

# 5. string.find(word)- The find() method is used to search for a word or letter inside a sentence. It tells us the position (index) where it starts.The find() method counts spaces too because they are also characters in a string.
s = "hello world"
print(s.find("world"))  # Output: 6

text = "Hello World"
print(text.find("World"))  # Output: 6

text = "I love Python"
position = text.find("P")
print(position)


# To check the Lenght of the character by using len function.
name = "vandana"
print(len(name))                          # to find length of character.
print(name.endswith("ana"))               # tells the variable string ends with the string "ana"
print(name.startswith("ana"))             # tells the variable string starts with the string "ana".
print(name.startswith("van"))             # tells the variable string starts with the string "van".
print(name.capitalize())                  # gives only first character string in capital form
print(name.count("a"))                    # tells total number of occurrences of any character.
print(name.find("dana"))                  # The find() method is used to search for a word or letter inside a sentence. It tells us the position (index) where it starts.

"""
Here are some of the "MOST USED STRING FUNCTION" in Python:

len() : Returns the length of the string.
lower() : Converts all characters to lowercase.
upper() : Converts all characters to uppercase.
strip() : Removes leading and trailing spaces.
replace(old, new) : Replaces a substring with another.
split(separator) : Splits the string into a list based on a separator.
join(iterable) : Joins elements of an iterable into a string.
find(substring) : Returns the index of the first occurrence of a substring.
startswith(prefix) : Checks if the string starts with a given prefix.
endswith(suffix) : Checks if the string ends with a given suffix.
"""

"""Most Used String Functions in Python:
Python provides several built-in string functions. Here are some of the most commonly used ones:
"""
# len() – Returns the length of a string.

text = "Hello"
print(len(text))  # Output: 5

# lower() – Converts a string to lowercase.

text = "HELLO"
print(text.lower())  # Output: hello

# upper() – Converts a string to uppercase.

text = "hello"
print(text.upper())  # Output: HELLO

# strip() – Removes leading and trailing spaces.

text = "  Hello  "
print(text.strip())  # Output: "Hello"

# replace() – Replaces a substring with another substring.

text = "Hello World"
print(text.replace("World", "Python"))  # Output: Hello Python

# split() – Splits a string into a list based on a delimiter.

text = "apple,banana,grape"
print(text.split(","))  # Output: ['apple', 'banana', 'grape']

# join() – Joins elements of a list into a string.

words = ["Hello", "World"]
print(" ".join(words))  # Output: Hello World

# find() – Returns the index of the first occurrence of a substring.

text = "Hello World"
print(text.find("World"))  # Output: 6

# count() – Counts occurrences of a substring.

text = "banana"
print(text.count("a"))  # Output: 3

# startswith() & endswith() – Checks if a string starts or ends with a given substring.

text = "Hello World"
print(text.startswith("Hello"))  # Output: True
print(text.endswith("Python"))  # Output: False



# We can use a "for" loop to write the table of 2 in Python like this:
for i in range(1, 11):  
    print(f"2 x {i} = {2 * i}")       # output:- 2 x 1 = 2; 2 x 2 = 4; 2 x 3 = 6;; 2 x 4 = 8; 2 x 5 = 10; 2 x 6 = 12; 2 x 7 = 14; 2 x 8 = 16; 2 x 9 = 18; 2 x 10 = 20


"""The code you wrote is not inside a function yet. But if you wrap it inside a function, it can be called a multiplication table function or simply a table generator function. Here's how you can define it:

def print_table(n):  
    for i in range(1, 11):  
        print(f"{n} x {i} = {n * i}")

# Calling the function for the table of 2
print_table(2)
This function is commonly called:-
- Multiplication table function
- Table generator function"""

