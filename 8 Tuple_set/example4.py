# example showing the concept of nested tuple 

mytuple = (
    (1,2,3),
    (4,5,6),
    (8,9,8)
)

print(len(mytuple))

for row in mytuple:
    for element in row:
        print(element,end=" ")
    print()