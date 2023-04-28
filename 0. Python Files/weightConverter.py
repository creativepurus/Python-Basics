weight = int(input("Enter Your Weight : "))
unit = input("(G)rams or (K)ilograms : ")
lower_unit = unit.lower()

if lower_unit == "g":
    new_weight = weight / 1000
    print(f"You are [{new_weight}] kilos.")
elif lower_unit == "k":
    new_weight = weight * 1000
    print(f"You are [{new_weight}] grams.")
else:
    print(f"Please type [G] for Grams or [K] for Kilograms...")