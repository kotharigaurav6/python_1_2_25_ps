# Basic Function 
# def show():
#     print("This is an example of function")
# show()

# default argument
# def show(name='Andrew Anderson'):
#     print("Hello "+name)
# show()
# show('Gaurav Kothari')

# def show(num1=10,num2=20):
#     print("Sum : ",(num1+num2))
# show()
# show(12,23)

# def show(name): # function with parameter
#     print("Hello "+name)
# show('Gaurav Kothari')  # positional argument

# def show(name,age): # function with parameter
#     print(f"Hello {name}, your age is {age}")
# show('Gaurav Kothari',56)  # positional argument

# keyword argument
def show(name,age): # function with parameter
    print(f"Hello {name}, your age is {age}")
show(age=67,name='Gaurav Kothari')  # keyword argument
