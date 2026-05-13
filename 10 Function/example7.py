# example showing the concept of recursion

# finding power of a number

b = int(input("Enter number : "))
e = int(input("Enter exponent : "))

def power(b,e):
    if e==0:
        return 1
    else :
        return b * power(b,e-1)

print("power of a number : ",power(b,e))