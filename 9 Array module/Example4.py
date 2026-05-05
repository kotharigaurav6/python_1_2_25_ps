# example showing the concept of array module
import array as arr
arrObj = arr.array("i",[1,2,3,4,5])
# arrObj = arr.array("i",[1,2,3,4,5,3,3,3,3,2,2,2,1,2,3,3])
# arrObj = arr.array("i",(1,2,3,4,5))
# arrObj = arr.array("i",{1,2,3,4,5})
# arrObj = arr.array("i",{1,2,3,4,5,2,2,2,2,2,4,4,4,5,5,8})
# arrObj = arr.array("u","Hello User")
# arrObj = arr.array("i",set([1,2,3,4,5]))
# arrObj = arr.array("i",set([1,2,3,4,5,2,2,2,2,2,3,3,4,5]))

print(arrObj)
print("type(arrObj) : ",type(arrObj))