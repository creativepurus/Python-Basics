# Car Game - Program of an Engine of a Car

# command = input("> ")
#
# while command.lower() != "quit":
#
#     if command.lower() == "help":
#         help_command = '''
#         start - to start the car
#         stop - to stop the car
#         quit - to exit the program
#         '''
#         print(help_command)
#
#     elif command.lower() == "start":
#         print("The car is started")
#
#     elif command.lower() == "stop":
#         print("The car is stopped")
#
#     elif command.lower() == "quit":
#         break
#
#     else:
#         print("Unknown command")

# ----------------------------------------------------------------

command = ""
is_Started = False

while True:

    command = input("> ").lower()

    if command == "start":
        if is_Started:
            print("The car is already started")
        else:
            is_Started = True
            print("The car is started...")

    elif command == "stop":
        if not is_Started:
            print("The car is already stopped")

        else:
            is_Started = False
            print("The car is stopped...")

    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit the program
        ''')

    elif command == "quit":
        break

    else:
        print("Unknown command")

