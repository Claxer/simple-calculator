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
    print("==============================")

    choice = input("Choose an operation (1-7): ")

    if choice in ["1", "2", "3", "4", "5", "6", "7"]:

        try:
            num1 = float(input("Enter the first value: "))
            num2 = float(input("Enter the second value: "))
        except ValueError:
            print("\n==============================")
            print("Invalid input. Please enter numbers only.")
            print("==============================")
            continue

        if choice == "1":
            print("Answer:", num1 + num2)

        elif choice == "2":
            print("Answer:", num1 - num2)

        elif choice == "3":
            print("Answer:", num1 * num2)

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Answer:", num1 / num2)

        elif choice == "5":
            print("Answer:", num1 ** num2)

        elif choice == "6":
            print("Answer:", num1 % num2)

        elif choice == "7":
            print("Answer:", num1 // num2)

    else:
        print("Invalid operation.")

    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

    if again != "yes":
            print("Program Ended.")
            break
