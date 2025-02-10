
"""
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""

class Person:
    def __init__(self,name ,age):
        self.name = name
        self.age=age
    # the __str__() function controlls what should be returned when the class object is represented as a string
    def __str__(self):
        return f"{self.name} aged {self.age}"

miles = Person("Isaac",50)
print(f"{miles.name} aged {miles.age}")

