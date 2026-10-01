
# IF ELSE AND ELIF IN PYTHON
"""If else and Elif statements are a multiway decision taken by our program due to certain conditions in our code."""

# If Elif else ladder use:

a = int(input("Enter your age: "))

if(a>=21):
    print("You are above the age of Consent")
    print("Good for you")
    
elif(a<0):
    print("You are entering invalid negative age.")
    
elif(a==0):
    print("You are entering 0, which is not valid age.")        
    
else:
    print("You are below the age of Consent")
    
    
print("End of Program")



# Quick Quiz: write a program to print yes when the age entered by the user is greater than or equal to 18.

age = int(input("Enter user's age: "))

if(age>=18):
    print("Yes! your age is greater than or equal to 18")
    print("GOod for you!")
    
else:
    print("Invalid, your age is not greater than or equal to 18")
    
print("End of code")

# RELATIONAL OPERATORS:
"""Relational Operators are used to evaluate conditions inside the if statements. Some examples of relational operators are:
==: equals.
> =: greater than/ equal to.
<=: lesser than/ equal to."""

# LOGICAL OPERATORS
"""In python logical operators operate on conditional statements. Example:
'and' - true if both operands are true else false.
'or' - true if at least one operand is true or else false.
'not' - inverts true to false & false to true."""

# ELIF CLAUSE
"""Elif in python means [else if] An if statements can be chained together with a lot of these Elif statements followed by an else statement."""
"""

if(condition1):
    print("yes")
    # Code   
elif(condition2):         #this ladder will stop once a condition in an if or elif is met.
    # code
    
elif(condition3):
    # code
elif(condition4):
    # code
    
else:
    #code"""

# IMPORTANT NOTES:
"""
1. There can be any number of elif statements.
2. Last else is executed only if all the conditions inside Elifs fail."""
