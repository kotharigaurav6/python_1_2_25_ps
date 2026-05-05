# example showing the concept of array module
# example to check whether entered array is palindrome or not

import array as arr
size = int(input("Enter no. of elements : "))
myArray = arr.array("i")

for i in range(size):
    value = int(input("Enter element : "))
    myArray.append(value)

print("Original Array : ")
for element in myArray:
    print(element,end=" ")

status = False
for i in range(0,size//2):
    if myArray[i] != myArray[size-1-i]:
        status = True
        break

if status:
    print("Array is not palindrome")
else:
    print("Array is palindrome")