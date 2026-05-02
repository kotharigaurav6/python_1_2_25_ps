# example showing the concept of tuple

num = (1,2,3,4,4,3,2,1,2)
print(len(num))
print(max(num))
print(min(num))
print(sum(num))

for n in num:
    print(n,end=" ")

print(4 in num)
print("4" in num)

# packing
student = ("Gaurav", 89,"Indore")
# unpacking 
name,age,city = student
print("Name : ",name)
print("age : ",age)
print("city : ",city)
