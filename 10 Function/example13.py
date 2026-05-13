# Higher Order Function
# Any function which returns or takes function as an argument, is known as Higher Order Function.

#  Callback : Python does support the concept of callback

# What is Callback ?
# A callback function is simply a function that is passed as an argument to another function and then called (executed) later.

# def anotherFunction(num):
#     return num*num
# print(anotherFunction(5))

# example-1
def outerFunction(callback):
    return callback()

def anotherFunction():
    return "This is an example of Higher order function"

print(outerFunction(anotherFunction))
