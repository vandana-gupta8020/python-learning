# 7. Write a program to print the following star pattern. 

"""

for n = 3

  *
 ***
*****

"""
# Takes input from the user — how many rows the pattern should have (for example, n = 3).
n = int(input("Enter the number: ")) 

for i in range(1, n+1):  # This 'for' loop runs from 1 to n (inclusive).🔹 Each 'i' represents the row number you're currently printing.
  print(" "* (n-i), end="")
  """🔹 Prints spaces before the stars.
🔹 The number of spaces needed decreases as i increases.
🔹 end="" prevents the line from breaking (so stars print on the same line).
For example
When i = 1, prints 2 spaces (n - i = 3 - 1 = 2)
When i = 2, prints 1 space
When i = 3, prints 0 space"""
  print("*"* (2*i-1), end="")       # print() gives a new line by default; we use argument end="" to avoid it temporarily.

  """🔹 Prints stars after the spaces.
🔹 The number of stars follows the pattern:
Row 1: 1 star
Row 2: 3 stars
Row 3: 5 stars
Which matches: 2*i - 1"""
  print("")
  """🔹 This moves the cursor to the next line after printing each row.
🔹 Even though we used end="" in previous lines, this line forces a new line."""