import math
import numpy as np
import curses

a = math.inputt()
#input student
Studentlist = []
print("Please input number of students:")
stunum = int(input())
print("Input info of student(Name and  DoB):")
Studentlist = a.number("Student", Studentlist, stunum)

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
mak = math.rounddown.roundmark(mark)

#GPA
stumarklist = np.zeros((stunum,4)) #input mark
for i in range (0, stunum): 
	stumarklist[i,0] = Studentlist[i,0]
	print("Student ", stumarklist[i,0])
	for j in range (1, 4):
	  mark = input()
	  stumarklist[i,j] = mark
		
GPAlist = np.zeros((stunum),2): #average GPA
for i in range (0, stunum):
	GPAlist[i,0] = stumarklist[i,0]
	print("GPA of student ",stumarklist[i,0])
	for j in range (1, 4):
		totalmark += int(stumarklist[i,j])
	GPAmark = totalmark/4
	GPAlist[i,1] = str(GPAmark)
		
#Sort student list by GPA descending
GPAlist = math.gpa.sort(GPAlist)






#module file(math.py)
class inputt:
    def number(x,name, listcc, amoun):
        for i in range(0, amoun):
            listt = listcc
            print(name+str(i+1))
            if (name == "Course"):
                listt.append("1")
                Info = input()
                listt[i] = Info
            else:
                listt.append([])
                for j in range (0, 2):
                    listt[i].append("1")
                    Info1 = input()
                    listt[i][j] = Info1
        return listt 

class list:
    def number(x,name,listcc):
        numlit = len(listcc)
        for i in range (0, numlit): 
            if(name =="Course"):
                print(name+str(i+1),":",listcc[i])
            else:
                for j in range(0, 2):
                    print(name+str(i+1),":",listcc[i][j])
       
class rounddown:
    def roundmark(mark1):
        mark2 = round(mark1, 1)
        return mark2
			
			
class gpa:		
    def sort(numbers):
        length = len(numbers)
        for i in range(0, length):
            for j in range(i + 1, length):
                if (int(numbers[i,1]) < int(numbers[j,1])):
                    a = numbers[i,1]
                    numbers[i,1] = numbers[j,1]
                    numbers[j,1] = a
     	            b = numbers[i,0]
                    numbers[i,0] = numbers[j,0]
                    numbers[j,0] = b
        return numbers    
	
	
	
	
	
	
	
	
