# example showing the concept of array module
import array as arr
size = int(input("Enter no. of elements : "))
myArray = arr.array("f")

for i in range(size):
    value = int(input("Enter element : "))
    myArray.append(value)

sum = 0
for element in myArray:
    sum += element
    print(element,end=" ")

print("Sum : ",sum)