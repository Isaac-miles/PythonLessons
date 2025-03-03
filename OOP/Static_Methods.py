
class Person:
    number_of_people = 0
    GRAVITY = -9.8
    
    def __init__(self, name):
        self.name = name
        Person.number_of_people +=1

p1 = Person("tim")
print(p1.number_of_people)

p2 = Person("jill")

print(p2.number_of_people)