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

print("keys : ",product.keys())
print("values : ",product.values())
print("items : ",product.items())
print("category name : ",product.get("category"))
print("category name : ",product.get("category_name"))
print("category name : ",product.get("category_name","Not Found"))

print("pop item : ",product.pop("category"))
print("product : ",product)

product.update({"quantity":10000})
print("product : ",product)

product.update({"quantity":10600})
print("product : ",product)

product.clear()
print(product)