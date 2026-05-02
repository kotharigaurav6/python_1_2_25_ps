# example showing the concept of list

myList = [14,25,37,46,54,36,27]

# logic-1
# myList.reverse()
# print("Reverse : ",myList,end=" ")

# logic-2
# print("Reverse : ",myList[::-1])

# logic-3
# for i in range(len(myList),0,-1): #it prints indexing
#     print(i,end=" ")

for i in range(len(myList),0,-1):
    print(myList[i-1],end=" ")


# logic-4
# len = len(myList)
# for i in range(len//2):
#     temp = myList[i]
#     myList[i] = myList[len-1-i]
#     myList[len-1-i] = temp 

# print("Reverse : ",myList)