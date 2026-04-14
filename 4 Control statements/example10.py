# example showing the concept of nested if else stateent

ch = input("Enter Nationality(i/I) for Indian : ")

if ch=='I' or ch=='i' :
   age = int(input("Enter age : "))
   if age>=18:
      print("Eligible to vote")
   else :
      print("Not eligible to vote")
else :
      print("Not an Indian")

