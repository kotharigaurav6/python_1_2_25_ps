# example showing the concept of list

# remove duplicate elements | print unique elements
myList = [3,1,2,2,2,2,2,3,3,3,2,2,1,1,1,4,4,4]
newList = []
for element in myList:
    if element not in newList:
        newList.append(element)
print("Unique element : ",newList)