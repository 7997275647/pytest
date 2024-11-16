
class TooManyStudents(Exception):
    pass
class classroom:
    def __init__(self, teacher, students, course):
        self.teacher = teacher
        self.students = students
        self.course = course

    def add_a_student(self,student):
        if len(self.students) <= 10:
            self.students.append(student)
        else:
            raise TooManyStudents


    def remove_student(self,name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break
    def change_teacher(self,new_teacher):
        self.teacher = new_teacher



class person:
    def __init__(self,name):
        self.name = name

class students(person):
    pass
class teachers(person):
    pass

