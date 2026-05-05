# example showing the concept of array module
# example to reverse an array

import array as arr
size = int(input("Enter no. of elements : "))
myArray = arr.array("i")

for i in range(size):
    value = int(input("Enter element : "))
    myArray.append(value)

print("Original Array : ")
for element in myArray:
    print(element,end=" ")

for i in range(0,size//2):
    temp = myArray[i]
    myArray[i] = myArray[size-1-i]
    myArray[size-1-i] = temp

print("\nReverse Array : ")
for element in myArray:
    print(element,end=" ")

# myArray.reverse()
# print(myArray)

