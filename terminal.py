while True:

    user_input = input("> ")
    command = user_input.lower().split()

    if not command:
        print("type something")
        continue


    if command[0] == "help":

        print("""
help
hello
calc
quit
""")


    elif command[0] == "hello":

        print("hello user")


    elif command[0] == "calc":

        operation = command[1]

        if operation == "add":

            answer = 0

            for number in command[2:]:

                answer = answer + int(number)

            print("answer =", answer)


    elif command[0] == "quit":

        print("closing terminal...")
        break


    else:
        print("unknown command")
