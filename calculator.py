import math

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
    print("8. Square Root")
    print("9. View History")
    print("10. Clear History")
    print("11. Save History")
    print("==============================")

    choice = input("Choose an operation (1-11): ")

    if choice == "9":
        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)

        print("==============================")

    elif choice == "10":
        history.clear()
        print("\n==============================")
        print("History cleared successfully.")
        print("==============================")

    elif choice == "11":

        with open("history.txt", "w") as file:

            if len(history) == 0:
                file.write("No calculations yet.\n")

            else:
                for item in history:
                    file.write(item + "\n")

        print("\n==============================")
        print("History saved to history.txt")
        print("==============================")

    elif choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:

        if choice == "8":
            try:
                num = float(input("Enter a number: "))

                if num < 0:
                    print("Error: Cannot find the square root of a negative number.")
                else:
                    answer = math.sqrt(num)
                    print("Answer:", answer)
                    history.append(f"√{num} = {answer}")

            except ValueError:
                print("\n==============================")
                print("Invalid input. Please enter a number.")
                print("==============================")

            continue

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
