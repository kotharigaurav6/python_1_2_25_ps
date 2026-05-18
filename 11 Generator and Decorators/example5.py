# example showing the concept of decorators

def my_decorator(myFun):
    def wrapper():
        print("statement 1")
        myFun()
        print("statement 2")
    return wrapper

@my_decorator
def say_hello():
    print("Hello World")

say_hello()

# @my_decorator
# def say_hello():

#  or

# say_hello = my_decorator(say_hello)
# say_hello = wrapper
# say_hello()