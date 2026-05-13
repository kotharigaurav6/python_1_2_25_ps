# program to find out grade

def getTotal():
    return m1+m2+m3+m4+m5

def getPercentage():
    return getTotal()/5

def getGrade():
    if per>=75 and per<=100:
        return 'A'
    else:
        if per>=60 and per<75:
            return 'B'
        else:
            if per>=50 and per<60:
                return 'C'
            else:
                if per>=33 and per<50:
                    return 'D'
                else:
                    return 'F'

m1,m2,m3,m4,m5 = map(int,input("Enter marks of 5 subjects : ").split())
# print(m1," ",m2," ",m3," ",m4," ",m5)

total = getTotal()
print("Total : ",total)

per = getPercentage()
print("Percentage : ",per)

grade = getGrade()
print("Grade ",grade)
