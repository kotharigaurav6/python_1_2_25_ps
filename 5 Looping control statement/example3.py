# while loop

num = int(input("Enter number : "))
count=0
while num>0:
    count+=1
    # num = num//10
    num = int(num/10)
print("No. of digits : ",count)