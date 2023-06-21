weight = float(input("Enter your Weight : "))

unit = input("(K)g or (L)bs : ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs : ", converted)

elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kgs : ", converted)

else:
    print("Invalid Input")
    