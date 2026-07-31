history = []

while True:
    print("\n==============================")
    print("      PYTHON CALCULATOR")
    print("==============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Modulus")
    print("7. Floor Division")
    print("8. View History")
    print("==============================")

    choice = input("Choose an operation (1-8): ")

    # View History
    if choice == "8":
        print("\n========== HISTORY ==========")

        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)

        print("=============================")

    elif choice in ["1", "2", "3", "4", "5", "6", "7"]:

        try:
            num1 = float(input("Enter the first value: "))
            num2 = float(input("Enter the second value: "))
        except ValueError:
            print("\n==============================")
            print("Invalid input. Please enter numbers only.")
            print("==============================")
            continue

        if choice == "1":
            answer = num1 + num2
            print("Answer:", answer)
            history.append(f"{num1} + {num2} = {answer}")

        elif choice == "2":
            answer = num1 - num2
            print("Answer:", answer)
            history.append(f"{num1} - {num2} = {answer}")

        elif choice == "3":
            answer = num1 * num2
            print("Answer:", answer)
            history.append(f"{num1} × {num2} = {answer}")

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                answer = num1 / num2
                print("Answer:", answer)
                history.append(f"{num1} ÷ {num2} = {answer}")

        elif choice == "5":
            answer = num1 ** num2
            print("Answer:", answer)
            history.append(f"{num1} ^ {num2} = {answer}")

        elif choice == "6":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                answer = num1 % num2
                print("Answer:", answer)
                history.append(f"{num1} % {num2} = {answer}")

        elif choice == "7":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                answer = num1 // num2
                print("Answer:", answer)
                history.append(f"{num1} // {num2} = {answer}")

    else:
        print("Invalid operation.")

    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

    if again != "yes":
        print("Program Ended.")
        break
