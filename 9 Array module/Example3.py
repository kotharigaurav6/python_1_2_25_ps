# example showing the concept of array module
import array as arr
arr1 = arr.array('i',[51,627,83,44,35,44,32,12,23,34,44])
print("type(arr) : ",type(arr1))
print(arr1)

print("Array index : ",arr1.index(627))
# print("Array index : ",arr1.index(300))

print("count : ",arr1.count(44))

print("Array buffer_info : ",arr1.buffer_info())
# output : (2676209719344, 11)
# First parameter : memmory address 
# Second parameter : length

x = arr1.tolist()
print("List : ",x)
print("type(x) : ",type(x))


# The formlist method in python is used with the array module to append elements from a list to an existing array. It ensures that data types of the array and the list are compatible
arrNew = arr.array('i',[1,2,3,4,5])
arrNew.fromlist(x)
print("arrNew : ",arrNew)

arr2 = arr.array('i',[65,66,67,68,69,70])
print("Array : ",arr2.tobytes())