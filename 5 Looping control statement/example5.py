# while loop
# example to check whether entered number is palindrome or not


num = int(input("Enter number : "))
rev = 0
temp = num
while num>0:
    rem = num % 10
    rev = rev * 10 + rem
    num = int(num / 10)

if rev == temp:
    print("Palindrome Number")
else : 
    print("Not a palindrome Number")

#  Hw
# check whether entered number is armstrong or not (while)
# program to check whether entered number is prime or not (for)