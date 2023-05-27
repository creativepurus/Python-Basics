secret_number = 5
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a no. between 0 & 9 : "))
    guess_count += 1
    if guess == secret_number:
        print("You Win !")
        break

    else:
        print("Try again...\n")