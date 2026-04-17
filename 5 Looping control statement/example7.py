# nested loop example

# for i in range(1,4):
#     for j in range(1,4):
#         print(i," ",j)

# for i in range(1,4):
#     print("i : ",i)
#     for j in range(1,4):
#         print("\tj : ",j)


# jump statements

# break : breaks the current loop

# for i in range(1,4):
#     print("i : ",i)
#     for j in range(1,4):
#         if i==2 and j==2:
#             break
#         print("\tj : ",j)

# continue : continues the current loop

for i in range(1,4):
    print("i : ",i)
    for j in range(1,4):
        if i==2 and j==2:
            continue
        print("\tj : ",j)

