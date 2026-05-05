#example showing the concept of set
# take dynamic input for set

n = int(input("Enter number of elements : "))
s = set()

for i in range(n):
    val = int(input("Enter element : "))
    s.add(val)

print("set : ",s)