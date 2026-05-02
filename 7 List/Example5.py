# example showing the concept of list

myList = [
    [1,2,3,4],
    [3,4,5],
    [5,6,7,8,9,9]
]
len = len(myList)
print("length : ",len)

# for i in range(len):
#     for j in myList[i]:
#         print(j,end=" ")
#     print()

# for i in myList:
#     print(i)

for i in myList:
    for element in i:
        print(element,end=" ")
    print()