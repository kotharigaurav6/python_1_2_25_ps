# def printData(m1,m2,m3,m4,m5):
#     print(m1+m2+m3+m4+m5)

# printData(1,2,3,4,5)

#variable length argument
# *args (multiple values)

def printData(*values):
    print("Sum : ",sum(values))

printData(1,2,3,4,5)
printData(1,2)
printData(1,2,3,4,5,5,6,7,7,8,8,8,88,9,9,9)