
class Employee:                  # Its base/ parent class
    company = "ITC"
    def show(self):
        print(f"The employee company's name is {self.company} and his salary is {self.company}")
    
class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages, here is your language: {self.language}")
  

class Programmer(Employee, Coder):                    # Its inherit class
    company = "ITC info tech"
    
    def show_language(self):
        print(f"The employee company's name is {self.company} and his salary is {self.language}")

a = Employee()
b = Programmer()


b.show()
b.printLanguages()
b.show_language()
