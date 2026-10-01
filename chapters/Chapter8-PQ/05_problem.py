# 5(a). Write a python function to print first n lines of the following pattern: 

"""

***
**               - for n = 3
*

"""
# define function for n lines...
def pattern(n):
    if(n==0):
        return          # Base case/ condition: stop recursion when n reaches 0
    print("*" * n)      # Print n stars on the current line
    pattern(n-1)        # Recursive call to print the next line with (n-1) stars

pattern(3)              # Call the function with n = 3

# SimpleExplaination
"""
- You give a number n (e.g., n = 3)
- The function prints n stars on the first line → ***
- Then it calls itself with n-1 → prints **
- Then again with n-2 → prints *
- When n becomes 0, the function stops (base case).

🔄 What Happens Internally (Dry Run for n = 3):

pattern(3) → prints ***
pattern(2) → prints **
pattern(1) → prints *
pattern(0) → stops
"""

# 5(b). Write a python function to print first n lines of the following pattern reverse version (bottom to top): 

"""
*
**            - for = 3
***
"""
# define recursive function for n lines
def pattern1(n, i=1):
    if(i > n):
        return          # base condition:  when i exceeds n, stop 
    print("*" * i)      # print on the way back up, starting from i = n to i = 1
    pattern1(n, i + 1)  # First recursive call (go all the way to the end)

pattern1(3)