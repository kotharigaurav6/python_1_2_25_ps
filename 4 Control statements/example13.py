# example to check whether entered character is in uppercase, lowercase, or a digit
# nested if else
ch = ord(input("Enter character : "))

if ch>=65 and ch<=90 :
   print("Character is in Uppercase")
else:
   if ch>=97 and ch<=122 :
      print("Character is in lowercase")
   else:
      if ch>=48 and ch<=57 :
         print("Character is a digit")
      else:
         print("Invalid Character")


# ASCII VALUE (American Standard Code for Information Interchange)
# a = 97, b = 98, ....... z = 122
#      |       |              |     = 32 (DIFFERENCE) 
# A = 65, B = 66, ....... Z = 90
# 0 = 48, 1 = 49, ....... 9 = 57