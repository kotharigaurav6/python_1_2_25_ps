# example showing the concept of array module
import array as arr
arr = arr.array('i',[51,627,83,44,35])
arr[2] = 10000
print(arr)

arr.append(10)
print("append : ",arr)

arr.extend([11,22,33])
print("extend : ",arr)

arr.reverse()
print("reverse : ",arr)

arr.insert(2,234)
print("insert : ",arr)

arr.remove(10000)
print("remove : ",arr)

print("pop: ",arr.pop())
print("pop: ",arr.pop(4))