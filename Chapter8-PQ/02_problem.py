# 2. Write a python program using function to convert Celsius to Fahrenheit.

"""
🌡️ 1. Celsius to Fahrenheit
Formula:-   fahrenheit = (celsius * 9/5) + 32

❄️ 2. Fahrenheit to Celsius
Formula:-   celsius = (fahrenheit - 32) * 5/9
"""

# f = int(input("Enter temperature in fehrenheit: "))
# c = (f-32)* 5/9

# print(c)

# Function to convert Celsius to Fahrenheit
def c_to_f(f):
    return (c * 9/5) + 32

# Take input in celsius and convert
c = float(input("Enter temperatur in celsius: "))
f = c_to_f(c)
# print(c_to_f(f))
print(f"{round(f, 2)}°F")      # rounded to 2 decimal places



# 2. Write a python program using function to convert Fahrenheit to Celsius.


# Function to convert Fahrenheit to Celsius
def f_to_c(c):
    return (f-32) * 5/9

# Take input in Fahrenheit and convert
f = float(input("Enter temperature in fehrenheit: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")       # rounded to 2 decimal places

