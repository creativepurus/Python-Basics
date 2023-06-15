coordinates = (1,2,3)

# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# print(x, y, z)

# --> Simple way to do the above task is 'Unpacking' which is specially in Python

x, y, z = coordinates
print(x, y)
print(z)

# --> Unpacking also works with List & Sets along with Tuples

coordinates = [4,5,6]
x, y, z = coordinates
print(x, y, z)

coordinates = {7,8,9}
x, y, z = coordinates
print(x, y, z)
