# example showing the concept of decorators

def my_decorator(myFun):
    def wrapper():
        print("statement 1")
        myFun()
        print("statement 2")
    return wrapper

# original function
def say_hello():
    print("Hello World")

# using decorator manually
say_hello = my_decorator(say_hello)
say_hello()