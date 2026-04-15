# example to find out grade (Nested if else)

# m1 = float(input("Enter marks of m1 : "))
# m2 = int(input("Enter marks of m2 : "))
# m3 = int(input("Enter marks of m3 : "))
# m4 = int(input("Enter marks of m4 : "))
# m5 = int(input("Enter marks of m5 : "))

m1,m2,m3,m4,m5 = map(int,input("Enter marks of 5 subjects : ").split())

# input("Enter marks of 5 subjects : ")
# "67 78 87 76 67"

# .split()
# ['67', '78', '87', '76', '67']

# map(int,...)
# [67, 78, 87, 76, 67]

# m1,m2,m3,m4,m5 = [67, 78, 87, 76, 67]
# now,the concept of sequence unpacking takes place and we get
# m1 = 67, m2 = 78, m3=87, m4=76, m5=67

total = m1+m2+m3+m4+m5
print("Total : ",total)

per = total/5
print("Percentage : ",per)

if per>=75 and per<=100 :
   print("Grade A")
else:
   if per>=60 and per<75 :
      print("Grade B")
   else:
      if per>=50 and per<60 :
         print("Grade C")
      else:
         if per>=33 and per<50 :
            print("Grade D")
         else:
            print("Fail")


