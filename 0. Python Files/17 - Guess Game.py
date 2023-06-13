secret_number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a number: "))
    guess_count += 1

    if guess == secret_number:
        print("Congrats! You Win!!!")
        break

    elif 5 <= guess <= 10:
        print("You are close to the Secret Number")

    elif guess < 5:
        print("Your guess is too low.")

    elif guess > 10:
        print("Your guess is too high.")

else:
    print("\nOops! You have reached the maximum limit of ", guess_limit,  "guesses! Try Again.")

