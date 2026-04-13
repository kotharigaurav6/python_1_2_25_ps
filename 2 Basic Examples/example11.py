# Dictionary (dict)
stud1 = {
    "name" : "Gaurav Kothari",
    "age" : 78,
    "address" : {
        "city":"Indore",
        "state":"Madhya Pradesh"
    }
} 
stud1["pincode"] = 452010

print("stud1 : ",stud1)
print("name : ",stud1["name"])
print("city : ",stud1["address"]["city"])
print("state : ",stud1["address"]["state"])
print("pincode : ",stud1["pincode"])

