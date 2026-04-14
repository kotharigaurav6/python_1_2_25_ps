# Program to find out area of triangle by herons formula

import math
a=10 
b=8 
c=6
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))  
print("Area of triangle : ",area)
