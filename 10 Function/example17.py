# callback

def printData(callback1,callback2):
    print("Statement 1")
    callback1()
    print("Statement 2")
    callback2()
    print("Statement 3")

def fun1():
    print("func1 method executes")

def fun2():
    print("func2 method executes")

printData(fun1,fun2)