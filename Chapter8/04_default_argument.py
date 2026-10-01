# DEFAULT PARMETER VALUE
"""
- We can have a value as default argument in a function.
- If we specify name "stranger" in the line containing def, this value is used when no argument is passed.
Example:"""
def greet(name = "stranger"):
    print("Hello", name)
    
greet()         # name will be "stranger" in function body (default)
greet("harry")    # name will be "harry" in function body (passed)
 
# 📝 Additional Notes:
"""Default Parameters:
In Python, you can assign default values to function parameters.
If a value is not provided for a parameter with a default value during the function call, Python uses the default.
Programiz
# Function Flexibility:
Using default parameters allows functions to be called with varying numbers of arguments, enhancing flexibility.
"""

def goodDay(name, ending="Thank You"):
    print(f"Good Day, {name}")
    print(ending)
    
goodDay("Vandana", "Thanks")
goodDay("Jyoti")

# 🔍 Step-by-Step Explanation:
# Function Definition:
def goodDay(name, ending="Thank You"):
 """This line defines a function named goodDay that accepts two parameters:
name: A required parameter.
ending: An optional parameter with a default value of "Thank You".
"""

# Function Body:
print(f"Good Day, {name}")
"""
Prints a greeting message incorporating the provided name.
"""
print(ending)  # Prints the ending message.

# Function Calls:

goodDay("Vandana", "Thanks")
"""
name is provided as "Vandana".
ending is provided as "Thanks".
"""
"""Output:
Good Day, Vandana
Thanks
goodDay("Jyoti")
name is provided as "Jyoti".
ending is not provided, so it defaults to "Thank You".

Output:
Good Day, Jyoti
Thank You
"""

# Define a function named 'goodDay' that takes two parameters:
# 'name' (required) and 'ending' (optional with a default value)
def goodDay(name, ending="Thank You"):
    # Print a greeting message with the provided 'name'
    print(f"Good Day, {name}")
    # Print the 'ending' message
    print(ending)

# Call the 'goodDay' function with both 'name' and 'ending' arguments
goodDay("Vandana", "Thanks")

# Call the 'goodDay' function with only the 'name' argument
# Since 'ending' is not provided, it will use the default value "Thank You"
goodDay("Jyoti")
