# print 2d array like structure

rows = int(input("Enter rows : "))
cols = int(input("Enter columns : "))

arr = []
for i in range(rows):
    row=[]
    for j in range(cols):
        value = int(input("Enter element : "))
        row.append(value) 
    arr.append(row)

for row in arr:
    for element in row:
        print(element,end=" ")
    print()