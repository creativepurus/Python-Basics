command = ""
started = False

print("\nThis is a car game ! Type 'help' to know more ...")

while True:
    
    command = input("> ").lower()

    if command == "start":
        if started:
            print(" Car has already started")
        else:
            started = True
            print(" Car has started... Ready to go !\n")

    elif command == "stop":
        if not started:
            print(" Car is already stopped !")
        else:
            started = False
            print(" Car has stopped !")

    elif command == "quit":
        print(" Car shut down !")
        exit()

    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to stop the car
        ''')
    else:
        print(" Sorry, I didn't understand... Try again !\n")