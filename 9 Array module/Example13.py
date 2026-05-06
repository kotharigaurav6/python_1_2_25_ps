# implementing multi dimensional array like structure
import array
num = int(input("Enter no. of matrix"))
rows = int(input("Enter rows : "))
cols = int(input("Enter columns : "))

arr = []

for n in range(num):
    print(f"\n Enter elements for Matrix {n+1} : ")

    matrix = []
    for i in range(rows):
        row = array.array("i")
        for j in range(cols):
            value = int(input(f"Enter elements [{i}][{j}] : "))
            row.append(value)
        matrix.append(row)

    arr.append(matrix)

# print result 
for n in range(num):
    print(f"\nMatrix {n+1} : ")
    for row in arr[n] :
        for val in row:
            print(val,end=" ")
        print()
    print()