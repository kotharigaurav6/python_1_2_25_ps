# example to find out all the perfect numbers between two entered numbers

n = int(input("Enter initial number : "))
m = int(input("Enter final number : "))

for i in range(n,m+1):
    sum = 0;
    for j in range(1,i//2 + 1):
        if i%j == 0:
            sum = sum + j;
    if i==sum :
        print(i,end=" ")