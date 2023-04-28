price = 1000000

good_credit = 0

if good_credit:
    new_price = 0.1 * price
else:
    new_price = 0.2 * price
print(f"Down Payment : ${new_price}")