# example showing the concept of list

size = int(input("Enter size : "))
myList = []

for i in range(size):
    value = int(input("Enter element : "))
    myList.append(value)

print("List : ",myList)
len = len(myList)
min = myList[0]
max = myList[0]

for i in range(len):
    if min > myList[i]:
        min = myList[i]
    if max < myList[i]:
        max = myList[i]

print("minimum element : ",min)
print("maximum element : ",max)
