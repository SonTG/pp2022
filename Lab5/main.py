import pack.math 
import numpy as np
import defoop
#import curse


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
Courselist = pack.math.inputt.number("Course", Courselist, cournum)

#list

print("Student's list")
print("Name")
print(pack.math.list.number("Student",Studentlistname))

print("Course's list")
print(pack.math.list.number("Course",Courselist))

#rounddown 
mark = float(input())
mak = rounddown.roundmark(mark)

#GPA
marklist = np.zeros((stunum,4))
GPAlist = np.zeros((stunum,2))
marklist = pack.math.markGPA.mGpa(marklist, Studentlist, stunum)
GPAlist = pack.math.markGPA.mGpa(GPAlist, Studentlist, stunum)

marklist = pack.math.markGPA.inputmark(marklist, stunum)
for i in range (0, stunum):
     makk = int(marklist[i ,1]) + int(marklist[i ,2]) + int(marklist[i ,3])
     GPAlist[i, 1] = str(makk)

#file
file = open("course.txt", "w")
for i in range(0, cournum):
    f = Courselist[i]
    file.write(f)
file.close()

file = open("student.txt", "w")
for i in range(0, stunum):
    stuin4 = defoop.oopStuin4(Studentlist[i,0], Studentlist[1])
    file.write(stuin4)
file.close()

file = open("mark.txt", "w")
for i in range(0, stunum):
    stumak = defoop.oopMak(GPAlist[i, 0], GPAlist[i, 1])
    file.write(stumak)
file.close()