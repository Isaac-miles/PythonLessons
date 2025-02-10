
"""
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""

class Person:
    def __init__(self,name ,age):
        self.name = name
        self.age=age
    # the __str__() function controlls what should be returned when the class object is represented as a string
    def __str__(self):
        return f"username is {self.name} aged {self.age}"
    def updateUsername(self,name):
        self.name = name

miles = Person("Isaac",50)
# print(f"{miles.name} aged {miles.age}")
miles.updateUsername("Helene")
print(miles)

#update object property
miles.age = 13
# delete object properties
del miles.age

class Colors:
    pass

