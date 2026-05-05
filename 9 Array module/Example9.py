# Important concept
# Python does not have a built-in "true 2d array" like in c, c++ or in java
# It uses : 
#    a. List of Lists
#    b. NumPy

# print 2d array like structure
arr = [
    [1,2,3],
    [3,4,5],
    [6,7,8]
]

for row in arr:
    for element in row:
        print(element,end=" ")
    print()