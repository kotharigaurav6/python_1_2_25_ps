# example showing the concept of list

# List
# List is mutable
# List is represented by square brackets 
# List can contains heterogenous elements as well

myList = [1,2,3,4,5,6]
print(myList)

# indexing
print("myList[0] : ",myList[0])
print("myList[3] : ",myList[3])
print("myList[5] : ",myList[5])
print("myList[-3] : ",myList[-3])

myList = [1,True,"Andrew",4.6,-345,6]
print(myList)
myList[2] = "Hello User"
print(myList)

# list slicing
print("myList[1:4] : ",myList[1:4])
print("myList[::2] : ",myList[::2])

# list method
myList.reverse()
print("Reverse : ",myList)

# myList = [5444,56,678,6,3212,23]
# myList.sort() #it requires homogenous list elements
# print("Ascending order : ",myList)

# myList.sort(reverse=True)
# print("Descending Order : ",myList)

myList.append(123)
print("Append : ",myList)

myList.insert(3,5000)
print("Insert : ",myList)

myList.remove(5000)
print("Remove : ",myList)

print("Pop out element : ",myList.pop())
print("After pop : ",myList)

myList.pop(2)
print("pop(2) : ",myList)

myList.extend([23])
print("extend : ",myList)
