# cube root 
# a = 5
# b = 1/3
# res = a ** b
# print("res : ",res)

# pow() vs math.pow() 

# pow() = integer | float 
# pow() = modulo  
# pow() = built-in function
# pow() = Most preferable in python
 
a = pow(2,3)
print("a : ",a)

b = pow(2,1/2)
print("b : ",b)

c = pow(5,3,2)  #modulo
# (5^3)%2
print("c : ",c)

# math.pow() = float 
# math.pow() = modulo concept is not allowed  
# math.pow() = for using pow function, we need to import math 

import math
a = math.pow(2,3)
print("a : ",a)

b = math.pow(2,1/2)
print("b : ",b)
