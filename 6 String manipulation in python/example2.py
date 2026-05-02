# string reverse
str = "This is an example of string"

temp=''
for ch in str:
    temp = ch + temp 

print("Reverse string : ",temp)