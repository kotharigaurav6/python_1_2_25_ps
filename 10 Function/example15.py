# example-4

def gotoroom(callback):
    print("gotoroom")
    callback(wonprize)

def removegarbage(callback):
    print("removegarbage")
    callback()

def wonprize():
    print("wonprize")

gotoroom(removegarbage)
