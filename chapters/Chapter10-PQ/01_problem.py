# 1. Create a Class "Programmer" for storing information of few programmers working at Microsoft.


class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
    
p = Programmer("Deepak", "120000", "110041")
print(p.company, p.name, p.salary, p.pin)


r = Programmer("Jyoti", "130000", "110086")
print(r.company, r.name, r.salary, r.pin)