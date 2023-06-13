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
for i in range(100):
    print(i)