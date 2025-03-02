
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
        self.students = []

    def add_student(self, student: Student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        print(value/len(self.students))

s1 = Student('Miles',19,95)
s2 = Student('Enoch',21,75)
s3 = Student('Emeka',18,65)

java_course = Course('Java',2)
java_course.add_student(s1)
java_course.add_student(s2)

print(java_course.students[0].name)
