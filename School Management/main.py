from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

# School create from user input
school_name = input("Enter School Name: ")
school_location = input("Enter School Location: ")
school = School(school_name, school_location)

# Add Classrooms
num_classrooms = int(input("How many classrooms? "))
for i in range(num_classrooms):
    class_name = input(f"Enter name for classroom {i+1}: ")
    classroom = ClassRoom(class_name)   
    school.add_classroom(classroom)    



num_students = int(input("How many students? "))
for i in range(num_students):
    student_name = input(f"Enter name for student {i+1}: ")
    class_choice = input(f"Enter classroom name for {student_name}: ")


    classroom = school.classrooms.get(class_choice, None)

    if classroom:
        student = Student(student_name, classroom)
        school.student_admission(student)
    else:
        print(f"Classroom {class_choice} not found! Skipping {student_name}...")

        classroom = next((c for c in school.classrooms if c.name == class_choice), None)
        if classroom:
            student = Student(student_name, classroom)
            school.student_admission(student)
        else:
            print(f"Classroom {class_choice} not found! Skipping {student_name}...")


num_teachers = int(input("How many teachers? "))
teachers = []
for i in range(num_teachers):
    teacher_name = input(f"Enter name for teacher {i+1}: ")
    teacher = Teacher(teacher_name)
    teachers.append(teacher)

# Add Subjects
num_subjects = int(input("How many subjects? "))
for i in range(num_subjects):
    subject_name = input(f"Enter name for subject {i+1}: ")

    # Assign teacher
    print("Choose teacher for this subject: ")
    for j, t in enumerate(teachers, 1):
        print(f"{j}. {t.name}")
    teacher_index = int(input("Enter teacher number: ")) - 1
    teacher = teachers[teacher_index]

    subject = Subject(subject_name, teacher)

    # Assign to classroom
    class_choice = input(f"Enter classroom name for subject {subject_name}: ")

    # dict থেকে classroom object আনা
    classroom = school.classrooms.get(class_choice, None)

    if classroom:
        classroom.add_subject(subject)
    else:
        print(f"Classroom {class_choice} not found! Skipping subject {subject_name}...")

# Take exams
for classroom in school.classrooms.values():
    classroom.take_semester_final_exam()


print(school)
