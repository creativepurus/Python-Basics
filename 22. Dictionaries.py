customer = {
    "name" : "Abc Xyz",
    "age" : 20,
    "is_verified" : True
}

print(customer["name"])

# print(customer["birthdate"])

# ERROR : Traceback (most recent call last):
#   File "d:\1. GitHub Repo\1. My Repositories\Python-Basics\0. Python Files\22. Dictionaries.py", line 9, in <module>
#     print(customer["birthdate"])
#           ~~~~~~~~^^^^^^^^^^^^^
# KeyError: 'birthdate'

# To remove the 'KeyError' , we use the 'get' keyword :
print(customer.get("birthdate"))
# Output : None

# We can also update the values :
print(customer.get("birthdate", "1 Jan 1800"))

customer["birthdate"] = "2 Jan 1900"
print(customer["birthdate"])
