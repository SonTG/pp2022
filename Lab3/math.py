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

class markGPA:
    def mGpa(li1, li2, num):
        for i in range (0, num):
            li1[i,0] = li2[i]
        return li1
    def inputmark(li, num):
        for i in range (0, num):
            li[i, 1] = input()
            li[i, 2] = input()
            li[i, 3] = input()
        return li
