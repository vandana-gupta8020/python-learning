
# FUNCTIONS WITH ARGUMENTS
"""
- A function can accept some value it can work with. We can put these values in the parentheses.
- A function can also return value as shown below:
"""
def greet(name):
    gr = "hello"+ name
    return gr
a = greet("harry")
print(a)         #a will now contain "hello harry"


# This function is named 'goodDay' and takes two inputs: 'name' and 'ending'
def goodDay(name, ending):
    # Prints a greeting message using the 'name' provided. Prints a greeting message by concatenating the string "Good Day " with the value of name.
    print("Good Day " + name)            # Prints a thank you message
    print(ending)               # Calling the function with the arguments "Vandana" and "Thanks"
    return "Done"     # Return the string "Done" to indicate completion. Returns the string "Done" to the caller. This allows the function to send a value back to the part of the program where it was called.
goodDay("Vandana", "Thanks")


a = goodDay("Vandana", "Thanks")
print(a)
