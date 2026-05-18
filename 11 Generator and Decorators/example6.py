# example showing the concept of decorators

def my_decorator(myFun):
    def wrapper(name):
        print("statement 1")
        myFun(name)
        print("statement 2")
    return wrapper

@my_decorator
def say_hello(name):
    print("Hello ",name)

name = "Andrew Anderson"
say_hello(name)

# @my_decorator
# def say_hello():

#  or

# say_hello = my_decorator(say_hello)
# say_hello = wrapper
# say_hello()