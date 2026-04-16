###################################### table of a number

# num = int(input("Enter number : "))
# for i in range(1,11):
#     print(num," x ",i," = ",num*i)

###################################### factorial of a number 

# num = int(input("Enter number : "))
# fact=1
# for i in range(1,num+1):
#     fact = fact * i
# print("Factorial : ",fact)

##################################### factors of a number

# num = int(input("Enter number : "))
# for i in range(1,num+1):
#     if num % i == 0 :
#         print(i,end=" ")

###################################### sum of n natural numbers 

num = int(input("Enter number : "))
sum=0
for i in range(1,num+1):
    sum = sum + i
print("Sum : ",sum)

# Hw
# print n even numbers
# print even numbers upto n
# print n odd numbers
# print odd numbers upto n
# 1     4       9       16      25 .....
# 1     8       27      64      125.....
# 1/1   1/2     1/3     1/4 ......
# sum of 1/1 +  1/2   +  1/3  +   1/4 ......
# 1     2      4      7      11     16 .....
# fibonacci series