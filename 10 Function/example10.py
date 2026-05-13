# Iterable : An iterable is any object you can loop over (like list,tuple, string etc)
# Iterator : An iterator is an object that gives values one by one using next()
# enumerate() Function : Adds index + value while looping
# zip() Function : combines multiple lists element-wise

# iterable
mylist = [1,2,3,4,5]
for i in mylist:
    print(i,end=" ")

# iterator 
myList = (10,20,30,40,50)
obj = iter(myList) #  convert iterable ---> iterator
print(type(obj)) #<class 'tuple_iterator'>
print("\nelement :  ",next(obj))
print("element :  ",next(obj))
print("element :  ",next(obj))
print("element :  ",next(obj))
print("element :  ",next(obj))

myList = [10,20,30,40,50]
obj = iter(myList) #  convert iterable ---> iterator
print(type(obj)) #<class 'list_iterator'>
print("\nelement :  ",next(obj))
print("element :  ",next(obj))
print("element :  ",next(obj))
print("element :  ",next(obj))
print("element :  ",next(obj))

# enumerate
myListItem = ["Soap","Fairness Cream","Oil"]
for value in enumerate(myListItem):
    print(" Value : ",value)

for index,value in enumerate(myListItem):
    print("Index : ",index," Value : ",value)

# zip function
names = ["Gaurav","Andrew","Peter"]
marks = [56,67,78]
address = ["Indore","Ujjain","Bhopal"]

result = zip(names,marks,address)
# print(result)
# print(type(result)) 
print(list(result))
print(type(list(result)))

