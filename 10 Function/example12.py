# lambda function (Anonymous function)

# printResult = lambda a,b: a+b 
# print(printResult(4,5))

myList = [13,2,34,456,43,3,9]
# myList.sort()
# myList.sort(reverse=True)
print(myList)


# when we use map(), it simply returns a map object (an iterator), not a list
printMap = map(lambda x: x*x,myList)
print(printMap)
print(type(printMap)) # <class 'map'>
print(list(printMap))
print(type(list(printMap))) # <class 'list'>

# map
res1 = list(map(lambda x: x*x,myList))
print("map : ",res1)

# filter
res2 = list(filter(lambda x: x*x <10,myList))
print("filter : ",res2)

# sorted
res2 = sorted(map(lambda x: x*x,myList))
print("sorted : ",res2)

#reduce
from functools import reduce
myList = [1,2,3,4,5]
res = reduce(lambda a,b : a+b, myList)
print(res)
