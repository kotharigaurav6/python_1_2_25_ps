# f"" = represents formatted string (preferrable)
# round = only for calculation, not for formatting 
# format() = older alternative

a = 53.3
print("a : ",a)
print("a : ",round(a,2))
print(f"a : {a:.2f}")
print("a : ","{:.2f}".format(a))

# =============================

name = "Gaurav"
age = 50 
print("My name is ",name," and my age is ",age)
print(f" My name is {name} and my age is {age}")