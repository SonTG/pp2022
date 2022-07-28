import math
import numpy as np
import curse

a = math.inputt()
#input student
Studentlist = []
print("Please input number of students:")
stunum = int(input())
print("Input info of student(Name and  DoB):")
Studentlistname = a.number("Student", Studentlist, stunum)

#input course
Courselist = []
print("Please input number of courses:")
cournum = int(input())
print("Input info of course:")
Courselist = a.number("Course", Courselist, cournum)

#list
b = math.list()
print("Student's list")
print("Name")
print(b.number("Student",Studentlistname))

print("Course's list")
print(b.number("Course",Courselist))

#rounddown 
mark = float(input())
mak = module1.roundmark(mark)

marklist = np.zeros((stunum,4))
GPAlist = np.zeros((stunum,2))
marklist = math.markGPA.mGpa(marklist, Studentlist, stunum)
GPAlist = math.markGPA.mGpa(GPAlist, Studentlist, stunum)

marklist = math.markGPA.inputmark(marklist, stunum)
for i in range (0, stunum):
     makk = int(marklist[i ,1]) + int(marklist[i ,2]) + int(marklist[i ,3])
     GPA[i, 1] = str(makk)
