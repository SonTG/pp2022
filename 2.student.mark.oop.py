class Course:
    def __init__(self, name, mark, number):
        self._name = name
        self._mark = mark
        self._number = number

    def get_name(self):
        return self._name

    def get_mark(self):
        return self._mark

    def get_number(self):
        return self._number

class Student:
    def __init__(self, student_id, name, dob):
        self._id = student_id
        self._name = name
        self._dob = dob
        self._course_list = []

    def set_course(self, course_list):
        self._course_list = course_list

    def print_student_data(self):
        print()
        print("-Name: ", self._name)
        print("-ID: ", self._id)
        print("-DoB: ", self._dob)

    def print_course_data(self):
        for course in self._course_list:
            print("-Course name: ", course.get_name())
            print("-Course mark: ", course.get_mark())
            print("-Course number: ", course.get_number())
            print()

def input_student(student_count):
    student_list = []
    for i in range(student_count):
        name = input("Name:")
        student_id = input("ID:")
        dob = input("DoB:")
        student_list.append(Student(student_id, name, dob))
    return student_list

def input_course(course_count):
    course_list = []
    for i in range(course_count):
        course_name = input("Enter course name:")
        course_mark = input("Enter course mark:")
        course_number = input("Enter course number:")
        course_list.append(Course(course_name,course_mark,course_number))
    return course_list

def main():
    student_count = int(input("Numbers of students: "))
    student_list = input_student(student_count)

    for student in student_list:
        course_count = int(input("Numbers of courses: "))
        course_list = input_course(course_count)
        student.set_course(course_list)

    for student in student_list:
        student.print_student_data()
        student.print_course_data()

main()