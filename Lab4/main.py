import pack.math 
import numpy as np
import curse


#input student
Studentlist = []
print("Please input number of students:")
stunum = int(input())
print("Input info of student(Name and  DoB):")
Studentlistname = pack.math.inputt.number("Student", Studentlist, stunum)

#input course
Courselist = []
print("Please input number of courses:")
cournum = int(input())
print("Input info of course:")
Courselist = a.inputt.number("Course", Courselist, cournum)

#list

print("Student's list")
print("Name")
print(b.list.number("Student",Studentlistname))

print("Course's list")
print(b.list.number("Course",Courselist))

#rounddown 
mark = float(input())
mak = rounddown.roundmark(mark)

marklist = np.zeros((stunum,4))
GPAlist = np.zeros((stunum,2))
marklist = pack.math.markGPA.mGpa(marklist, Studentlist, stunum)
GPAlist = pack.math.markGPA.mGpa(GPAlist, Studentlist, stunum)

marklist = pack.math.markGPA.inputmark(marklist, stunum)
for i in range (0, stunum):
     makk = int(marklist[i ,1]) + int(marklist[i ,2]) + int(marklist[i ,3])
     GPA[i, 1] = str(makk)
