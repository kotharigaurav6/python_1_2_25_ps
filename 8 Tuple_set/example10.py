#example showing the concept of set

s1 = {1,2,3,4,5}
s2 = {3,4,5,6}

print("s1 : ",s1)
print("s2 : ",s2)

c = s1.intersection(s2)
# returns new set
# does not change original
print("c : ",c)
print("s1 : ",s1)

print()

c = s1.intersection_update(s2)
# returns None
# modifies original set
print("c : ",c)
print("s1 : ",s1)

