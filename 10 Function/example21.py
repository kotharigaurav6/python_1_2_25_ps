# Example showing the concept of closure

# def outerFunction():
#     def innerFunction():
#         print("This is inner Function")
#     innerFunction()
# outerFunction()


# def outerFunction():
#     def innerFunction():
#         print("This is an example of inner function")
#     return innerFunction
# myFun = outerFunction()
# myFun()


# def outerFunction():
#     name = "Andrew Anderson"
#     def innerFunction():
#         print("Hello ",name)
#     innerFunction()
# outerFunction()


def outerFunction():
    fname = "Andrew"
    def innerFunction(lname):
        print("Hello ",fname,lname)
    return innerFunction
myFun = outerFunction()
myFun(" Anderson")