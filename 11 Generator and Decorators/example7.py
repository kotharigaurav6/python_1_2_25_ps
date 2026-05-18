# example showing the concept of decorators

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

def my_decorator(myFun):
    def wrapper(a,b):
        print("Before")
        res = myFun(a,b)
        print("After")
        return res
    return wrapper

@my_decorator
def add(a,b) :
    return a + b

print("Addition : ",add(a,b))