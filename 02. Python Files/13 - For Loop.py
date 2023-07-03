numbers = [1,2,3,4,5,7]

print("\nUsing For Loop : ")
for i in numbers:
    print(i)


print("\nUsing While Loop : ")
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print("Using Range function")
for i in range(10):
    print(i)

prices = [10,20,30]
total = 0
for price in prices:
    total += price

# print(total)
print("\nUsing For Loop to calculate the price : ")
print(f"Total Price : {total}")

for x in range(4):
    for y in range(3):
        print(f"X: {x} Y: {y}")

numbers = [5,2,5,2,2]
for num_count in numbers:
    print(num_count * 'x')
print()

numbers = [5,2,5,2,2]
for num_count in numbers:
    output = ''
    for count in range(num_count):
        output += 'x'
    print(output)
print()

numbers = [2,2,2,2,5]
for num_count in numbers:
    output = ''
    for count in range(num_count):
        output += 'x'
    print(output)
