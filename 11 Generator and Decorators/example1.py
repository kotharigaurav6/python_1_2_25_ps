# example showing the concept of generator function

def show():
    yield(1)
    yield(2)
    yield(3)
    
result = show()
print("result : ",result)
print("type(result) : ",type(result))
print(next(result))
print(next(result))
print(next(result))

