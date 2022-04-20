#storing info
Students=[]
Courses=[]
class student:
    #Store
    def __init__(self, ID = None, name = None, DoB = None, course_name = None, course_mark = None):
        self.name = name
        self.id = ID
        self.date = DoB
        self.coursename = course_name
        self.coursemark = course_mark
    
    #Add
    def addInfo(self):
        self.name = input("Input name: ")
        self.id = input("Input ID: ")
        self.date = input("Input DoB: ")

    #Describe
    def list(self):
        print("-Name:",self.name)
        print("-ID:",self.id)
        print("-DoB:",self.date)

    #Course info
    def setCourse(self):
        self.coursename = input("Enter course name:")
        self.coursemark = input("Enter course mark:")
    
    #List course
    def listCourse(self):
        print("-Course name:",self.coursename)
        print("-Course mark:",self.coursemark)
        
  
#driver
a=int(input("Numbers of students:"))
for i in range(0,a):
    Student=student()
    Student.addInfo()
    Students.append(Student)
    b=int(input("Numbers of courses:"))
    for n in range(0,b):
        Student=student()
        Student.setCourse()
        Courses.append(Student)
    print("")

print("Student's info list:")   
for Student in Students:
    Student.list()
    print("Student's course info:")
    for Student in Courses:
        Student.listCourse()
        print("")
    print("")
