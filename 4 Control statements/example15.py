# switch is not directly supported in python
# we can achieve the functionality of switch by three ways : 
#  1. if elif els
#  2. match 
#  3. Dictionary

num = 2
match num:
    case 1 : 
        print("One Statement");
    case 2 : 
        print("Two Statement");
    case 3 : 
        print("Three Statement");
    case _ : 
        print("Invalid Statement");

