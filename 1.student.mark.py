stlist = []
clist = []
def class_input():
    print("Input class:\n")
    n = int(input("Enter number of students: "))
    for i in range(0, n):
        student = {}
        sid = int(input("Student ID: "))
        name = input("Name: ")
        dob = input("Date of birth: ")
        student["ID"] = sid
        student["Name"] = name
        student["Date of birth"] = dob
        stlist.append(student)
    print("\n")
def course_input():
    print("Input course:\n")
    m = int(input("Enter number of courses: "))
    for i in range(0, m):
        cid = int(input("Course ID: "))
        cname = input("Course name: ")
        clist.append({"ID": cid,"Name": cname})
    print("\n")
def marks_input():
    print("Input marks:\n")
    courseid = int(input("Enter course ID: "))
    for i in range(0, len(clist)):
        course = clist[i]
        if courseid == course["ID"]:
            for j in range(0, len(stlist)):
                student = stlist[j]
                student[course["Name"]] = float(input("Enter mark for student " + str(student["ID"]) + ": "))
    print("\n")
def list_courses():
    print("Course list:\n")
    print("ID\tName")
    for i in range(0, len(clist)):
        course = clist[i]
        print(str(course["ID"])+"\t"+str(course["Name"]))
    print("\n")
def list_students():
    print("Student list:\n")
    print("ID\tName\tDate of birth")
    for i in range(0, len(stlist)):
        student = stlist[i]
        print(str(student["ID"])+"\t"+str(student["Name"])+"\t"+str(student["Date of birth"]))
    print("\n")
def show_marks():
    print("Show a course' marks:\n")
    courseid = int(input("Enter course ID: "))
    print("ID\tMark")
    for i in range(0, len(clist)):
        course = clist[i]
        if courseid == course["ID"]:
            for j in range(0, len(stlist)):
                student = stlist[j]
                print(str(student["ID"])+"\t"+str(student[course["Name"]]))
    print("\n")
class_input()
course_input()
marks_input()
list_courses()
list_students()
show_marks()