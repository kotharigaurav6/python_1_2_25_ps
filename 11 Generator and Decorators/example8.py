# example showing the concept of decorators

def decorator1(myFun):
    def wrapper():
        print("Decorator 1")
        myFun()
    return wrapper

def decorator2(myFun):
    def wrapper():
        print("Decorator 2")
        myFun()
    return wrapper 

@decorator1
@decorator2
def say_hello():
    print("Multiple decorators")

say_hello()

# say_hello = decorator1(decorator2(say_hello))
# say_hello = wrapper
# say_hello()
# myFun = decorator2(say_hello)
# myFun = wrapper
# myFun()

# Note : 
# Decorators are applied bottom ---> top
# Execution happens top ---> botttom