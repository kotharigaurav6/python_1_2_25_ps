# example to find out grade (Nested if else)

m1,m2,m3,m4,m5 = map(int,input("Enter marks of 5 subjects : ").split())

total = m1+m2+m3+m4+m5
print("Total : ",total)

per = total/5
print("Percentage : ",per)

if per>=75 and per<=100 :
   print("Grade A")

elif per>=60 and per<75 :
   print("Grade B")

elif per>=50 and per<60 :
   print("Grade C")

elif per>=33 and per<50 :
   print("Grade D")

else:
   print("Fail")


