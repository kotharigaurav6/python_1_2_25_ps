# program to check whether entered string is palindrome or not

str = "NitiN"
print("Original String : ",str)
str=list(str)
len = len(str)
status = True
for i in range(0,len//2+1):
    if str[i] != str[len-1-i]:
        status = False 
        break

if status:
    print("String is palindrome")
else: 
    print("String is not palindrome")
