numbers = [100,20,23,532,123,9234,1324,1235]
max = numbers[0]

for num in numbers:
    if num > max:
        max = num
print(f"Maximum number from the list: {numbers} is {max}")
