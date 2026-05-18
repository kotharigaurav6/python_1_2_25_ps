# example showing the concept of exception

# 1. ValueError
# wrong value, correct type 
# try:
#     x = int("abc")
# except ValueError: 
#     print("Invalid Value")


# 2. TypeError
# wrong type used in operation 
# try:
#     x = 10 + "25"
# except TypeError: 
#     print("Type Mismatch")


# 3. ZeroDivisionError
# division by zero 
# try:
#     x = 10 / 0
# except ZeroDivisionError: 
#     print("Cannot divide by zero")


# 4. IndexError
# List index out of range 
# try:
#     l = [1,2,3]
#     print(l[5])
# except IndexError: 
#     print("Index out of range")


# 5. KeyError
# Dictionary key not found 
# try:
#     d = {"a":1}
#     print(d["b"])
# except KeyError: 
#     print("Key not found")


# 6. NameError
# variable not defined 
# try:
#     print(x)
# except NameError: 
#     print("Variable not defined")


# 7. FileNotFoundError
# File does not exist 
# try:
#     f = open("data.txt")
# except FileNotFoundError: 
#     print("File not found")


# 8. AttributeError
# Object have no such attribute 
# try:
#     x = 10
#     x.append(5)
# except AttributeError: 
#     print("Invalid Attribute")

# 9. Exception (General catch)
# Catch any error
try:
    x = int("abc")
except Exception as e: 
    print("Error : ",e)
