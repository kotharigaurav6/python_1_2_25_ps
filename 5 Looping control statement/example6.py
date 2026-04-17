# do while loop is not supported by python but its functionalty is achieved by while True + break

while True:
    password = input("Enter password : ")
    if len(password)>6:
        print("Invalid")
    else :
        print("Valid")
        break