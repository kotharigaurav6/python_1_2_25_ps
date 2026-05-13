# function with no argument and no return type
# def getSum():
#     num1 = int(input("Enter first number : "))
#     num2 = int(input("Enter second number : "))
#     print("Sum : ",num1+num2)
# getSum() # no argument


# function with no argument and with return type
# def getSum():
#     num1 = int(input("Enter first number : "))
#     num2 = int(input("Enter second number : "))
#     return num1+num2
# print("Sum : ",getSum()) # no argument


# function with argument and no return type
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# def getSum(num1,b):
#     print("Sum : ",num1+b)
# getSum(num1,num2) # with argument


# function with argument and with return type
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def getSum(num1,b):
    return num1+b
print("Sum : ",getSum(num1,num2)) # with argument