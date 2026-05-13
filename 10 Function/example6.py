# example showing the concept of recursion

# factorial of a number

num = int(input("Enter number : "))

def fact(n):
    if n==0:
        return 1
    else :
        return n * fact(n-1)

print("Factorial of a number : ",fact(num))