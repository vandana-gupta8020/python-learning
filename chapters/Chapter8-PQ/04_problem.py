# 4. Write a recursive function to calculate the sum of first n natural numbers.

"""
sum(1) = 1
sum(2) = 1+2=3
sum(3) = 1+2+3=6
sum(4) = 1+2+3+4=10
sum(5) = 1+2+3+4+5=15
sum(n) = 1+2+3+4+5+.........+(n-1) + n
sum(n) = sum(n-1)+n

"""
# In Python:- difference b/w '/'  &  '//'
"""
'/' = Its called 'Floating type division.' Which gives us floating value.
'//' = Its called 'Floor Divivsion', which gives us integer type value and removes decimal part, and gives the whole number.
"""


# comparison between the Formula Method and Recursive Method for calculating the sum of first n natural numbers:
"""
|   Feature           	     |    Formula Method	                        | Recursive Method                                        |                              
|     ---                    |              ---                             |                ---                                      |
|   Approach	             |    Uses a direct mathematical formula	    | Uses recursion (function calls itself)                  |
|   Syntax	                 |    sum = n * (n + 1) // 2	                | return n + sum_natural(n - 1)                           |
|   Time                     |    Complexity	O(1) (Constant time)	    | O(n) (Linear time)                                      |
|   Space                    |    Complexity	O(1) (No extra space used)	| O(n) (Uses stack memory for recursive calls)            |
|   Performance	             |    Very fast, best for large n	            | Slower for large n, can hit recursion limit             |
|   Ease of Understanding	 |    Simple and direct	                        | Conceptually useful for understanding recursion         |
|   Best Use Case	         |    When performance is important	            | When learning recursion / breaking down steps           |
|   Limitation	             |    Only works when you know the formula	    | Slower, can cause stack overflow if n is large          |

"""
n = int(input("Enter a natural number: "))  # take input form user
# define function for sum of natrual no.
def sum_natural(n):
    if(n<1):  
        return 0         # Base case/ condition for invalid input
    elif(n==1):
        return 1         # Base case/ condition: sum of 1 is 1
    else:
        return n + sum_natural(n - 1)        # Recursive step
    
    # Check if input is valid
if n < 1:
    print("Invalid input. Please enter a number greater than or equal to 1.")
else:
    result = sum_natural(n)
    print(f"Sum of first {n} natural numbers is: {result}")
    
    
# ------------------------OR---------------------------

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(4))