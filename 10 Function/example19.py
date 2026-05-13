# example showing the concept of callback hell | Pyramid of doom

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

def addition(a,b,callback):
    print("Addition : ",a+b)
    callback(True)
def subtraction(a,b,callback):
    print("Subtraction : ",a-b)
    callback(False)
def multiplication(a,b,callback):
    print("Multiplication : ",a*b)
    callback()

addition(a,b,lambda value:
    subtraction(a,b,lambda value : 
            multiplication(a,b,lambda :
                print("End of program")               
            ) if not value else None    
    ) if value else None    
)

