# Program to remove duplicate characters from string

str = "This is an example of Programming"
temp = ''
for ch in str:
    if ch not in temp:
        temp = temp + ch
print("After removing duplicate characters : ",temp)
# program to count unique characcters in a string
print("unique characters : ",len(temp))
