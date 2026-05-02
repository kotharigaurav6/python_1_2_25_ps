# example showing the concept of dictionary
product={
    "category":"Electronics",
    "name":"Fan",
    "pid":999011,
    "variant":{
        "name":"Variant1",
        "price":65000
    } 
}

print("product : ",product)
print("type(product) : ",type(product))
print("category : ",product["category"])
print("name : ",product["name"])
print("variant name : ",product["variant"]["name"])
print("variant price : ",product["variant"]["price"])



