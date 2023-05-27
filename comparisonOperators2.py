name = input("Write Your Name : ")
len_name = len(name)

print(len_name)

if len_name < 3:
    print("Name must be altease 3 characters long...")
elif len_name > 30:
    print("Name must not exceed 30 characters...")
else:
    print(f"Hello [{name}] :)")