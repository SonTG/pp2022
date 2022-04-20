#storing info
students = []
student = {
    "id" : None,
    "name" : None,
    "DoB" : None,
    "Course ID" : None,
    "Course name" : None,
    "Course mark" : None
}

#input function
def addStudent():
    numStudent = int(input("Number of students: "))
    for i in range(numStudent):
        student = {
            "id" : input("id: "),
            "name" : input("name: "),
            "DoB" : input("DoB: "),
            "Course ID" : input("Course ID: "),
            "Course name" : input("Course name: "),
            "Course mark" : input("Course mark: ")
        }
        students.append(student)

#list function
def listStudent():
    print("The number of student(s) in class is: %s" % len(students))
    for i in students:
        print("Student info: ", i)

#driver
if __name__ == "__main__":
    addStudent()
    listStudent()