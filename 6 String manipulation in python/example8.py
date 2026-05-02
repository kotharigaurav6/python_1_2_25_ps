# Program to convert string into Upper case

str = "This is an example of string in python"
result = ''
for ch in str :
    if ord(ch)>=97 and ord(ch)<=122:
        result += chr(ord(ch)-32)
    else:
        result+=ch
print("Upper case : ",result)