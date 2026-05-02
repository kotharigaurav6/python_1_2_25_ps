# string reverse
str = "This is an example of string"
print("Original String : ",str)
str=list(str)
# print(len(str))
# print(str[0])
len = len(str)
for i in range(0,len//2+1):
    temp = str[i]
    str[i] = str[len-1-i]
    str[len-1-i] = temp 

print("Reverse String : ","".join(str)) #result is returned as a new string
