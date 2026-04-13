# bytes  #immutable
x = bytes({65,66,67})
print("x : ",x)
print("type(x) : ",type(x))

x = bytes({65,66,67,66,66,67})
print("x : ",x)
print("type(x) : ",type(x))

x = bytes([65,66,67,66,66,67])
print("x : ",x)
print("type(x) : ",type(x))

# bytearray #mutable
x = bytearray({65,66,67})
print("x : ",x)
print("type(x) : ",type(x))

x = bytearray({65,66,67,66,66,67})
x[2] = 100
print("x : ",x)
print("type(x) : ",type(x))

x = bytearray([65,66,67,66,66,67])
print("x : ",x)
print("type(x) : ",type(x))

# -------------------------------------

print(list("ABC"))
print(list(b'ABC'))

# -----------------------

b = bytes([97,98,99])
mv = memoryview(b)
print("mv[1] : ",mv[1])