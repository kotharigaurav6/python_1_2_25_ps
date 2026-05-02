#     *
#    **
#   ***
#  ****
# *****

# row = int(input("Enter rows : "))
# for i in range(1,row+1):
#     for sp in range(1,row-i+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# *****
#  ****
#   ***
#    **
#     *

row = int(input("Enter rows : "))
for i in range(row,0,-1):
    for sp in range(1,row-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end="")
    print()