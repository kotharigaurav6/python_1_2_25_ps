# example showing the concept of tuple

# mytuple = (45,56,65,54,43,34)
mytuple = (45,-56,6.5,45,"Hello",43,True,45)
print(mytuple)
print("type(mytuple) : ",type(mytuple))
print(mytuple[0])
print(mytuple[4])
print(mytuple[-4])

# tuple slicing
print(mytuple[1:4])
print(mytuple[-4:-1])
print(mytuple[::4])

# methods
x = mytuple.count(45)
print("count of 45 : ",x)

# y = mytuple.index(45)
y = mytuple.index("Hello")
print("y : ",y)
