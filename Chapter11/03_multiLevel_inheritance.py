class Employee:
    a = 1


class Programmer(Employee):
    b = 2


class Manager(Programmer):
    c = 3
    
    
object = Employee()
print(object.a)          # prints the 'a' attribute 
# print(object.b)          # Shows an error there is no 'b' attribute in Employee class


o = Programmer()
print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)