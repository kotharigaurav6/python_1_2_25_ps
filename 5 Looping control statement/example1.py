# Looping control statement : 
# Looping is the process of performing same tak or some task in an iterative manner.

# python do not support do-while loop directly, but we can achieve the same behaviour using while True and break

# for i in range(10):
#     print("This is an example of python")

# for i in range(0,5):
#     print("This is an example of python")

# for i in range(1,6):
#     print("This is an example of python : ",i)

# range(n,m,step)
# range(initial value,m-1,increment | decrement by how much )

# for i in range(0,5,2):
#     print(i)

# for i in range(0,10,1):
#     print(i,end=" ")

# for i in range(10,0,-1):
#     print(i,end=" ")

list = ["apple", "mango", "banana"]
for fruit in list :
    print(fruit,end=" ")