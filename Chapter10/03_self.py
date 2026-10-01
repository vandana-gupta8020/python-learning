class Employee:
    name = "Vandana"
    language = "Python"  # this is class attribute
    salary = 300000
    
    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")
        
    
    @staticmethod         # decorator to make as a static method
    def greet():
        print("good Morning")

rohan = Employee()
rohan.name = "Rohan Roro Robinson"     # this is an instance(object) attribute
rohan.language = "Javascript"   # Instance attributes, take preference over class attributes during assignment & retrieval.

rohan.getInfo()
rohan.greet()