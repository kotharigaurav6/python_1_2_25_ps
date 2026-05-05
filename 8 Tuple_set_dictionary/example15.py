# example showing the concept of dictionary
# nested dynamic dictionary - taking input from user

info={}
size = int(input("Enter no. of pairs : "))

for i in range(size):
    key = input("Enter Key : ")
    value = input("Enter value : ")
    info[key] = {"age" : value} 
print(info)