# program to swap two numbers without using third variable

a = 5 
b = 6 
print('Before swapping :\na : ',a,'\nb : ',b)
# a = a + b
# b = a - b 
# a = a - b

# a = a * b
# b = int(a / b) 
# a = int(a / b)

a = a ^ b
b = a ^ b 
a = a ^ b

print("After swapping :\na : ",a,"\nb : ",b)