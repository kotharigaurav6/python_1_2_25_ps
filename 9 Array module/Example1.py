# example showing the concept of array module
import array
arr = array.array('i',[1,2,3,4,5])
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

arr = array.array('f',[1,2,3,4,5])
print(arr)

arr = array.array('d',[1,2,3,4,5])
print(arr)

# deprecated
arr = array.array('u',['1','2','3','4','5'])
print(arr)

# deprecated
arr = array.array('u',"Hello")
print(arr)

x = "Hello"
print("Array : ",list(x))