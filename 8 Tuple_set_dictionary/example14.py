# example showing the concept of dictionary
# dynamic value - taking input from user

info={}
size = int(input("Enter no. of pairs : "))

# for i in range(1,size):
for i in range(size):
    key = input("Enter Key : ")
    value = input("Enter value : ")
    info[key] = value 
print(info)