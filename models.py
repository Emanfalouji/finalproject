class Course:


    def __init__(self, course_name, course_level,course_id):
        self.course_id = course_id

        self.course_name = course_name
        self.course_level = course_level

    def print_info(self):
        print(str(self.course_id)+"  "+self.course_name+"  "+self.course_level)


class Student:


    def __init__(self, student_name, student_level,student_id):
        self.student_id = student_id

        self.student_name = student_name
        self.student_level = student_level
        self.courses_list = []

    def enroll_course(self, course):
        if self.student_level == course.course_level:
            for enrolled_course in self.courses_list:
                if course.course_id == enrolled_course.course_id:
                    print("Course already enrolled")
                    return  # Exit the method if the course is already enrolled
            self.courses_list.append(course)  # Add the course to the student's courses_list
            print("Course enrolled successfully")
        else:
            print("Invalid course class")

    def get_student_info(self):
        print (str(self.student_id)+"  "+self.student_name+"  "+self.student_level)

        if len(self.courses_list)==0:
            print ("Course list is EMPTY")
            return
        print("course List >>")
        for course in self.courses_list:
            print(course.course_name)











