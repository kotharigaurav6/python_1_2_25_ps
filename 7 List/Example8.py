# example showing the concept of list

# myDict = {}
# print(myDict.get(11)) #None
# print(myDict.get(11,0)) # 0

# finding out the frequency of elements
myList = [3,1,2,2,2,2,2,3,3,3,2,2,1,1,1,4,4,4]
myDict = {}
for element in myList:
   myDict[element] = myDict.get(element,0)+1   

print("Frequency : ",myDict)