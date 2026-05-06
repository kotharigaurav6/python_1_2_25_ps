# perform addition on two 2d like structure
import array
rows = int(input("Enter rows : "))
cols = int(input("Enter columns : "))

arr1 = []
# print(type(arr1))
print("Enter arr1 elements : \n")
for i in range(rows):
    row1=array.array("i")
    for j in range(cols):
        value = int(input("Enter element : "))
        row1.append(value) 
    arr1.append(row1)

arr2 = []
# print(type(arr2))
print("\nEnter arr2 element : \n")
for i in range(rows):
    row2=array.array("i")
    for j in range(cols):
        value = int(input("Enter element : "))
        row2.append(value) 
    arr2.append(row2)

arr3 = []
# print(type(arr3))
print("\nResultant elements : \n")
for i in range(rows):
    row3=array.array("i")
    for j in range(cols):
        value = arr1[i][j] + arr2[i][j]
        row3.append(value) 
    arr3.append(row3)

print("Array 1 : ")
for row in arr1:
    for element in row:
        print(element,end=" ")
    print()

print("Array 2 : ")
for row in arr2:
    for element in row:
        print(element,end=" ")
    print()

print("Array 3 : ")
for row in arr3:
    for element in row:
        print(element,end=" ")
    print()
