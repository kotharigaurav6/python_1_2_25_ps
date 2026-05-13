# example-2
# value = int(input("Enter value : "))
# def outerFunction(callback,value):
#     return callback(value)

# def anotherFunction(num):
#     return num*num

# print(outerFunction(anotherFunction,value))

# example-3
num = int(input("Enter number : "))
def outerFunction(callback):
    return callback
def anotherFunction(num):
    return num*num
f = outerFunction(anotherFunction)
print("Result : ",f(num))