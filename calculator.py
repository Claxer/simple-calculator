while True:
    print("Select an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1-4): ")

    if choice in ["1", "2", "3", "4"]:

        num1 = float(input("Enter the first value: "))
        num2 = float(input("Enter the second value: "))

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

    else:
        print("Invalid operation.")

    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

    if again != "yes":
            print("Program Ended.")
            break
