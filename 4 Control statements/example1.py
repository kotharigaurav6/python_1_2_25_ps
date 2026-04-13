######### program to get three numbers and print its average

# a = int(input('Enter value of a : '))
# b = int(input('Enter value of b : '))
# c = int(input('Enter value of c : '))
# sum = a+b+c
# print("Sum : ",sum)
# avg = sum/3
# print("Average : ",avg)

########################### convert temp from f to c 

# f = float(input("Enter temp in f : "))
# c = (f-32)*5/9
# print("Temp in c : ",c)

################### simple interest 

# p = int(input("Enter principal : "))
# r = float(input("Enter rate : "))
# t = int(input("Enter time : "))

# si = (p*r*t)/100
# print("Simple interest : ",si)

################ compound interest 

p = int(input("Enter principal : "))
r = float(input("Enter rate : "))
t = int(input("Enter time : "))
# amt = p * pow(1+r/100,t)
amt = p * (1+r/100) ** t
ci = amt - p 
print("Amount : ",amt)
print("Compound Interest : ",ci)