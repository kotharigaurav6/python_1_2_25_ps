# example showing the concept of list

myList = [1,2,3,4,5,6,7]
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
