# 6. Write a python function which converts inches to cms.


# define function for converting inches to cms
def inches_to_cms(inch):
    return inch * 2.54    # Note:- 1 Inch = 2.54 centimeters

# take input from user
n = float(input("Enter the value in Inches: "))

# print ouput
print(f"The corresponding value in cms is {inches_to_cms(n)}")