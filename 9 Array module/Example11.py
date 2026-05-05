# print 2d array like structure
# jagged array
rows = int(input("Enter rows : "))

arr = []
for i in range(rows):
    row=[]
    cols = int(input(f"Enter columns for {i+1} rows :"))

    for j in range(cols):
        value = int(input("Enter element : "))
        row.append(value) 
    arr.append(row)

for row in arr:
    for element in row:
        print(element,end=" ")
    print()