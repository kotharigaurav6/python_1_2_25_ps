#example showing the concept of set
# take dynamic input for set

s1 = set()
s2 = set()

print("For first set : ")
for i in range(int(input("Enter size : "))):
    val = int(input("Enter element : "))
    s1.add(val)

print("For second set : ")
for i in range(int(input("Enter size : "))):
    val = int(input("Enter element : "))
    s2.add(val)

print("set1 : ",s1)
print("set2 : ",s2)

print("Union : ",s1|s2)
print("Intersection : ",s1&s2)
print("Difference(s1-s2) : ",s1-s2)
print("Difference(s2-s1) : ",s2-s1)
