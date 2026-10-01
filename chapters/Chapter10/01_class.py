
class Employee:
    name = "Vandana"
    language = "Python"  # this is class attribute
    salary = 300000
    
vandana = Employee()
print(vandana.name, vandana.language)
    
    
    
vandana = Employee()
vandana.name = "vandana"   # this is an instance(object) attribute
print(vandana.language, vandana.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
rohan.language = "Javascript"   # Instance attributes, take preference over class attributes during assignment & retrieval.
print (rohan.salary, rohan.language)

# Here, 'name' is instance(object) attribute and 'salary' & 'language' are class attribute as the directly below to the class