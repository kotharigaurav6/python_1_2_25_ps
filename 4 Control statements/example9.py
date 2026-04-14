# example showing the concept of nested if else stateent

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if num1==num2 :
   print("Both are equal")
else :
   if num1>num2 : 
      print(num1," is greater")
   else :
      print(num2," is greater")