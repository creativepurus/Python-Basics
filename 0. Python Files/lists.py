'''matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][2] = 5
print(matrix[0][2])


for row in matrix:
    for column in row:
        print(matrix)
        '''

numbers = [1,3,2,3,4,5]

print(numbers.count(3))

numbers.sort()
numbers.reverse()
print(numbers)

numbers.append(20)

numbers.insert(2,10)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.pop()
print(numbers)

no = numbers.index(4)
print(no)

print(50 in numbers)

numbers.clear()
print(numbers)