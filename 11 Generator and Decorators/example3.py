# example showing the concept of generator expression

# generator = (i for i in range(5))
# print(generator)
# for i in generator:
#     print(i,end=" ")

# gen = (i for i in range(5))
# print(list(gen))

# gen = (i*i for i in range(5))
# print(list(gen))

# gen = (i for i in range(5) if i%2==0)
# print(list(gen))

# res = sum(i for i in range(5))
# print(res)

# res = (ch.upper() for ch in "Hello")
# print(list(res))

# gen = (i*j for i in range(1,3) for j in range(1,3))
# print(list(gen))

# res = "Hello"
# print(list(res))
# print(list(res))
# print(list(res))

gen = (i*i for i in range(5))
print(list(gen)) #[0, 1, 4, 9, 16]
print(list(gen)) #[]
