# *
# **
# ***
# ****
# *****

# row = int(input("Enter rows : "))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end="");
#     print()

# row = int(input("Enter rows : "))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(i,end="");
#     print()

# row = int(input("Enter rows : "))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j,end="");
#     print()

# row = int(input("Enter rows : "))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end="");
#     print()

row = int(input("Enter rows : "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(chr(128512+j),end="");
    print()