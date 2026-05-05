# What is comprehension ? 
# A short and smart way to create collection(list,set,dict) using a single line.

# set comprehension

# result = { x*x for x in range(1,11) }
# print(result)

# with condition
# result = {x*x for x in range(1,11) if x%2==0}
# print(result)

# with if else
result = { "Even" if x%2==0 else "Odd" for x in range(1,11) }
print(result)