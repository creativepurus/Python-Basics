matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(matrix[0][1])

# matrix[0][1] = 100
# print(matrix[0][1])

for row in matrix:
    print(row)

print()

for row in matrix:
    for element in row:
        print(element)