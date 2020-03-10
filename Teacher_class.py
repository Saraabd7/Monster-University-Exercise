from Monster_class import *

class Teacher(Monster):
    def __init__(self, first_name, last_name, teacher_id):
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.teacher_id = teacher_id

