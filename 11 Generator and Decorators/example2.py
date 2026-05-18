# example showing the concept of generator function

# def count(n):
#     for i in range(n):
#         yield i
# for num in count(5):
#     print(num,end=" ")


# num = int(input("Enter number : "))
# def evenNumbers(n):
#     for i in range(n):
#         if i%2==0:
#             yield i
# for num in evenNumbers(num):
#     print(num,end=" ")


# num = int(input("Enter number : "))
# def factors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             yield i
# for num in factors(num):
#     print(num,end=" ")


num = int(input("Enter number of terms : "))
def series(n):
    a = -1
    b = 1
    # for i in range(1,n+1):
    for _ in range(n):
        c = a + b
        yield c
        a = b
        b = c
for num in series(num):
    print(num,end=" ")
