# while loop
# reversing a number

num = int(input("Enter number : "))
rev = 0
while num>0:
    rem = num % 10
    rev = rev * 10 + rem
    num = int(num / 10)

print("Reverse Number : ",rev)