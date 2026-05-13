# example showing the concept of callback hell | Pyramid of doom

start = 10

def printData(value,callback):
    print(value,end=" ")
    callback(value+2)
    
printData(start,lambda value:
    printData(value,lambda value:
        printData(value,lambda value:
            printData(value,lambda _:
                print("End of program")
            )       
        )         
    )
)

# Output : 10   12  14  16  18 ......