from Monster_class import *


class Student(Monster):
    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.f_name = first_name
        self.l_name = last_name
        self.student_id = student_id
        self.skills = []


