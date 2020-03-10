from Monster_class import *
from Workshop_class import *
from Student_class import *
from Teacher_class import *
# i want to show that i can create a student with only first and last name

student1 = Student('Carmen', 'Harris', 1)
student2 = Student('John', 'Connor', 3)
#
# print(student1)
# print(student1.first_name, student1.last_name)
# print(student2)
# print(student2.first_name, student1.last_name)
# while True:
# student3 = Student(first_name, last_name, 3)
# print(student3.first_name + student3.last_name)
# for student in list_students_created:
# print(student1.f_name, student1.l_name, student2.f_name, student2.l_name)

print('Adding a student :: ')
students_list = []
student_id = 0
while True:
    student_id += 1
    first_name = input('Enter first name:\n')
    last_name = input('Enter last name:\n')
    skills = input('Enter skills:\n')
    student = Student(first_name, last_name, student_id)
    students_list.append(student)
    print(f'Student Name is {first_name} {last_name} {student_id}')
    print(students_list)
    print('Number of students in the list: ' + str(len(students_list)))
    print(f'Skills are {skills}')
    if first_name == 'Quit' or last_name == 'Quit':
        break

# teacher1 = Teacher('David', 'Bell', 1)
# teacher2 = Teacher('Clair', 'Hansel' 2)
# print(teacher1)
# print(teacher1.first_name, teacher1.last_name)
# print(teacher2)
# print(teacher2.first_name, teacher2.last_name)
# list_teachers_created = []
# list_teachers_created.append(teacher1)
# list_teachers_created.append(teacher2)
# for teacher in list_teachers_created:
# print(teacher1.first_name, teacher1.last_name, teacher2.first_name, teacher2.last_name)

print('Adding a teacher::')
teachers_list = []
teacher_id = 0
while True:
    teacher_id += 1
    first_name = input('Enter teacher first name:\n')
    last_name = input('Enter teacher last name:\n')
    teacher = Teacher(first_name, last_name, teacher_id)
    teachers_list.append(teacher)
    print(f'Teacher Name is {first_name} {last_name} {teacher_id}')
    print(teachers_list)
    print('Number of teachers in the list: ' + str(len(teachers_list)))
    if first_name == 'Quit' or last_name == 'Quit':
        break

print('Adding a workshop::')
workshop_list = []
while True:
    subject_name = input('Enter subject name:\n')
    teacher_name = input('Enter teacher name\n')
    attendees = input('Enter number of attendees\n')
    subject = workshop_monster(subject_name, teacher_name, attendees)
    workshop_list.append(subject)
    print(f'Workshop added was: {subject} and teacher\'s name is {teacher_name}. Attendees are {attendees}')
    print(workshop_list)
    print('Number of workshops in the list: ' + str(len(workshop_list)))
    if subject_name == 'Quit' or teacher_name == 'Quit' or attendees == 'Quit':
        break

print(workshop_list)

