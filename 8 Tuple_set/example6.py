#example showing the concept of set
s1 = {1,2,3,2,2,2,2}
s2 = {2,2,2,5,6,7,7,8}

print("union : ",s1 | s2)
print("union : ",s1.union(s2))

print("intersection : ",s1 & s2)
print("intersection : ",s1.intersection(s2))

print("difference : ",s1 - s2)
print("difference : ",s1.difference(s2))
print("difference : ",s2 - s1)
print("difference : ",s2.difference(s1))

s3 = {11,22,33,44,55}
s4 = s3.copy()
print(s4)

s3.clear()
print(s3)