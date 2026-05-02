#example showing the concept of set
# take dynamic input for set

# needs to take value in single line by seperating it with space
set1 = set(map(int,input("Enter first set elements : ").split()))
set2 = set(map(int,input("Enter second set elements : ").split())) 

print("set1 : ",set1)
print("set2 : ",set2)

print("union : ",set1|set2)
print("intersection : ",set1&set2)
print("difference : ",set1-set2)
