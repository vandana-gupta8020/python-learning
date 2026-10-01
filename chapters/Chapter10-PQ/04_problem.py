# 4. Add a static method in problem 2, to greet the user with hello.

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
        
    
    @staticmethod
    def hello():
        print("Hello there!")
         
a = Calculator(n)
a.square()
a.cube()
a.square_root()
a.hello()
