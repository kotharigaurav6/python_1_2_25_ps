# example showing the concept of array module
import array as arr
size = int(input("Enter no. of elements : "))
myArray = arr.array("i")

for i in range(size):
    value = int(input("Enter value : "))
    myArray.append(value)
# way - 1
print("Array elements are : ",myArray)

# way - 2
for element in myArray:
    print(element,end=" ")