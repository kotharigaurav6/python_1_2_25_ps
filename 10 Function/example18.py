# callback
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

def printData(callback,task,a,b):
    match task:
        case "addition":
            callback(a+b)
        case "subtraction":
            callback(a-b)
        case "multiplication":
            callback(a*b)
        case "division":
            callback(a//b)
        case _:
            print("Invalid Operation")

def printResult(result):    
    print("Result :  ",result)

task = "addition"
printData(printResult,task,a,b)