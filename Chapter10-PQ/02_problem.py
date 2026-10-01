# 2. Write a class "Calculator" capable of finding square, cube and square root of a number.

n = int(input("Enter a number: "))

class Calculator:
    def __init__(self, n):
        self.n = n
        
        
    def square(self):
        print(f"the square of {n} is {self.n*self.n}")
        
        
    def cube(self):
        print(f"The cube of {n} is {self.n*self.n*self.n}")
        
    def square_root(self):
        print(f"the square root of {n} is {self.n**1/2}")
         
a = Calculator(n)
a.square()
a.cube()
a.square_root()

