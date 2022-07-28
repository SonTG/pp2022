#input number of students in a class 
def input_no_student():
    global No_student 
    No_student = int(input("Number of students: "))

#input student info: id, name, DoB
def input_students_info():
    global tupleStudent
    for count in range (0,No_student):
        tempName = str(input("Name of student No"+ str(count+1) +": "))
        tempID = str(input("ID of student No"+ str(count+1) +": "))
        tempDoB = str(input("DoB of student No"+ str(count+1) +": "))
        tempDict = {
            "Name": tempName,
            "ID": tempID,
            "DoB": tempDoB
        }
        tupleStudent = list(tupleStudent)
        tupleStudent.append(tempDict)
        tupleStudent = tuple(tupleStudent)

def input_course_info():
    global tupleCourse
    for count in range (0,No_course):
        tempName = str(input("Name of course No"+ str(count+1) +": "))
        tempID = str(input("ID of course No"+ str(count+1) +": "))
        tempDict = {
            "Name": tempName,
            "ID": tempID
        }
        tupleCourse = list(tupleCourse)
        tupleCourse.append(tempDict)
        tupleCourse = tuple(tupleCourse)
