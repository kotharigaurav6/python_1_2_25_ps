# example of operators
# membership operator
#  checks the presence of an element in the sequence
list = [1,2,3,4,5]
print(3 in list)
print(3 not in list)

# Identity operator 
a = [1,2]
b = a 
c = [1,2]
print(a is b)
print(a is not b)
print(a is c)

# python do not have increment | decrement operator

a = "Hello User"
# a[start:stop:step]
print(a[::2])
print(a[::3])