class inputt:
    def number(name, listcc, amoun):
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
