# example of operators
# conditional operator

res = "Gets Entry" if True else "Not Allowed"
print("Res : ",res)

res = "Gets Entry" if False else "Not Allowed"
print("Res : ",res)

a = 5
b = 2
res = "a is greater" if a>b else "b is greater"
print(res)

res = str(a)+" is greater" if a>b else str(b)+" is greater"
print(res)