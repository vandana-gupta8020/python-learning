class Employee:
    language = "Python"  # this is class attribute
    salary = 300000
    
    def __init__(self, name, salary, language):     # dunder method which automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I'm creating an Object")
    
    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")
        
    
    @staticmethod         # decorator to make as a static method
    def greet():
        print("good Morning")

jyoti = Employee("Jyoti", "130000", "JavaScript")
# rohan.name = "Rohan Roro Robinson"
print(jyoti.name, jyoti.salary, jyoti.language)

# vandana = Employee()