from operator import truediv


class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade #0-100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = list

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False