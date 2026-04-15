# switch is not directly supported in python
# we can achieve the functionality of switch by three ways : 
#  1. if elif els
#  2. match 
#  3. Dictionary

day = 10
match day:
    case 1 | 7 : 
        print("Weekend")
    case 2 | 3 | 4 | 5 | 6: 
        print("WeekDays")
    case _ : 
        print("Invalid Statement")

