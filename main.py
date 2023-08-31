from models import Student,Course
student_list = []
course_list = []


def get_course_list(courses):
    print ("ID\t|\t Name\t|\tlevel")
    for course in courses:
        print(course.print_info())



def get_student_list(students):
    print("ID\t|\t Name\t|\tLevel")
    for student in students:
        print(student.get_student_info())


def find_student(student_id, students):
    index = 0
    for student in students:
        if student.student_id == str(student_id):
            return index
        index += 1
    return -1



def find_course(course_id, courses):
    print("ddd")
    index = 0
    for course in courses:

        if course.course_id == course_id :

            return index
        index += 1

    return -1



while True:
    print("\nMain Page")
    print("1. Add New Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Display all students")
    print("5. Create new Course")
    print("6. Add Course to student")
    choice = input("Select an option: ")
    if choice == '1':
        student_name = input("Enter student name")
        student_id = input("Enter student id:")
        while True:
            student_level = input("Select student level (A, B, C)")
            if student_level in ['A', 'B', 'C']:
                student = Student(student_name, student_level, student_id)
                student_list.append(student)
                print("Student created successfully.")
                break
            else:
                print("Invalid student level. Please select A, B, or C.")



    elif choice == '2':
        student_ID = int(input("Enter student ID: "))
        print(student_ID)

        student_index = find_student(student_ID, student_list)

        if student_index == -1:
            print("Student not found.")
        else:
            student_list.pop(student_index)
            print("Student removed successfully.")



    elif choice == '3':
        get_student_list(student_list)
        student_id = int(input("Enter student ID: "))
        student_index = find_student(student_id, student_list)
        if student_index == -1:
            print("Student not exist")
        else:
            student_name = input("Enter student name: ")
            while True:
                student_level = input("Select student level (A, B, C): ")
                if student_level in ['A', 'B', 'C']:
                    student_list[student_index].student_name = student_name
                    student_list[student_index].student_level = student_level
                    print("Student details updated successfully.")
                    break  # Break out of the loop after successful update
                else:
                    print("Invalid student level. Please select A, B, or C.")

    elif choice == '4':
        get_student_list(student_list)

    elif choice == '5':
            course_name=input("Enter course name")
            while True :
                course_level = input("Select course class(A,B,C)")
                course_id=input("enter the course id")
                if course_level in ('A' , 'B' , 'C' ):
                    break
                    course_id = len(course_list)+1
                    course = Course(course_id , course_name , course_level)
                    course_list.append(course)
                    print ("Course Created Successfuly")
    elif choice == '6':
        get_course_list(course_list)
        student_id = int(input("Enter student id: "))
        student_index = find_student(student_id, student_list)
        if student_index == -1:
            print("Student Not Exist")
        else:
            course_id = int(input("Enter Course ID: "))
            course_index = find_course(course_id, course_list)
            if course_index == -1:
                print("Course Not Exist")
            else:
                print("Enrolling student", student_id, "in course", course_id)
                student_list[student_index].enroll_course(course_list[course_index])

    elif choice == '6':
            get_course_list(course_list)
            student_id = int(input ("enter student id"))
            student_index = find_student(student_id,student_list)
            if student_index == -1:
               print("Student Not Exist")
            else:


                course_id = int(input("Enter Course ID:"))
                for course in courses:
                    print ("ddddddd")

                    if course.course_id == str(course_id):
                        print(course_id)
                        student_list[student_index].enroll_course(course_list[course_index])
                    else:
                        print ("dd")





                course_index = find_course(course_id, course_list)
                if course_index == -1:

                    print("Course Not Exist")
                else:

                    print(course_id)
                    student_list[student_index].enroll_course(course_list[course_index])


    else:
          exit()
























