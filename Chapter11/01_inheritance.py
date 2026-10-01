
class Employee:                  # Its base/ parent class
    company = "ITC"
    def show(self):
        print(f"The employee name is {self.name} and his salary is {self.salary}")
    
# class Programmer:
#     company = "ITC info tech"   
#     def show(self):
#         print(f"{self.name} and his salary is {self.salary}")
      
#     def show_language(self):
#         print(f"The employee name is {self.name} and his salary is {self.salary}")
  

class Programmer(Employee):                    # Its inherit class
    company = "ITC info tech"
    
    def show_language(self):
        print(f"The employee name is {self.name} and his salary is {self.salary}")

a = Employee()
b = Programmer()

print(a.company, b.company)


