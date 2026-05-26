while True:
    command = input("> ")
    parts = command.split()

    if not parts:
        print("type something")
        continue

    if parts[0].lower() == "help":
        print("""
help
calc
hello
quit
""")

    elif parts[0].lower() == "quit":
        print("closing terminal...")
        break

    elif parts[0].lower() == "hello":
        print("hello user")

    elif parts[0].lower() == "calc":

        print("""
1. add
2. subtract
3. multiply
4. divide
""")

        operation = input("choose operation: ")

        if operation == "add":

            num1 = int(input("first number: "))
            num2 = int(input("second number: "))

            answer = num1 + num2

            print("answer =", answer)

    else:
        print("unknown command")
