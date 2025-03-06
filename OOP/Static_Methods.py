
class Person:
    number_of_persons = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.number_of_persons +=1

    @classmethod
    def number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
       cls.number_of_people +=1


p1 = Person("tim")
p2 = Person("jill")

class Math:

    @staticmethod
    def add5(x):
        return  x + 5

print(Math.add5(5))