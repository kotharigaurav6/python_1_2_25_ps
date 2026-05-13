# Note : 
# Important Rule : 
# You can mix both, but positional arguments must come first

def show(name,age): # function with parameter
    print(f"Hello {name}, your age is {age}")
#show('Gaurav Kothari',age=45)  # positional argument comes first then keyword argument comes
# show(age=45,'Gaurav Kothari')  invalid
# show(name = 'Gaurav Kothari',45) invalid
# show(45,'Gaurav Kothari') # output not correct