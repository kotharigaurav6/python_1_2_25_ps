# example showing the concept of tuple

n = int(input("Enter number of elements : "))
data = []

for i in range(n):
    val = input("Enter elements : ")
    data.append(val)

t = tuple(data)
print("Dynamic tuple : ",t)