# Sequence datatype
# common features of sequence datatype

# Indexing -> s[0]
# Slicing -> s[1:3]
# Iteration -> for
# Length-> len()
# Membership -> in 

# string 
str = "Hello"
print("str : ",str)

# 0   1   2   3   4
# H   e   l   l   o
# -5 -4  -3  -2  -1 

print("str[-3:-1] : ",str[-3:-1])
print("str[3:5] : ",str[3:5])

# ------------------------------

x = range(0,5)
for i in x :
    print(i)

# ------------------------------

t = (10,20,30)
print("length of tuple : ",len(t))
print(t * 3)

# ------------------------------

print(3 in [1,2,3,4,5])

# -----------------------------

t = (1,[2,3,4])
t[1][0] = 1000
print(t)

# -----------------------------

a = [1,2]
a.append([3,4])  #[1, 2, [3, 4]]
print(a)

b = [1,2]
b.extend([3,4]) #[1, 2, 3, 4]
print(b)