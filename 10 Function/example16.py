num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def printData(a,b,callback):
    sum = a + b 
    callback(sum)

def result(res):
    print("Result : ",res)

printData(num1,num2,result)
