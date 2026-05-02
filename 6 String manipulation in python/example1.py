# example showing the concept of string manipulation(string handling)

str = "this is an example of string manipulation"
# string indexing
print("str[0]  : ",str[0])
print("str[7]  : ",str[7])
print("str[-8]  : ",str[-8])

# string slicing
print("str[0:5]  : ",str[0:5])
print("str[7:12]  : ",str[7:12])
print("str[-8:-3]  : ",str[-8:-3])
print("str[::3]  : ",str[::3])
print("str[::-3]  : ",str[::-3])

# string methods
print("lowercase : ",str.lower())
print("uppercase : ",str.upper())
print("isdigit : ",str.isdigit())
print("islower : ",str.islower())
print("isnumeric : ",str.isnumeric())
print("isupper : ",str.isupper())
print("replace : ",str.replace("example","King"))
print("split : ",str.split())
print("split : ",type(str.split()))
print("capitalize : ",str.capitalize())
print("join : ","-".join(str))

# string formatting
name = "Gaurav"
age = 50
print("Hello ",name," your age is ",age)
print(f"Hello {name} your age is {age}") #formatted string (Recommended)
print("Hello {} your age is {}".format(name,age)) # now in newer versions format is alternative or is less preferred
