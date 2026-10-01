
class Employee:
    name = "Vandana"
    language = "Python"  # this is class attribute
    salary = 300000
    

rohan = Employee()
rohan.name = "Rohan Roro Robinson"     # this is an instance(object) attribute
rohan.language = "Javascript"   # Instance attributes, take preference over class attributes during assignment & retrieval.
print (rohan.salary, rohan.language)

# Here, 'name' is instance(object) attribute and 'salary' & 'language' are class attribute as the directly below to the class

"""
NOTE: Instance attributes, take preference over class attributes during assignment & retrieval.
 When looking up for vandana.attribute it checks for the following:
  - Is attributes present in object?
  - Is attributes present in class?
"""