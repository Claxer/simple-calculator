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
    print("9. Percentage")
    print("10. Factorial")
    print("11. Cube Root")
    print("12. Absolute Value")
    print("13. Reciprocal (1/x)")
    print("14. Pi (π)")
    print("15. Euler's Number (e)")
    print("16. Logarithm (log₁₀)")
    print("17. Natural Logarithm (ln)")
    print("18. Sine (sin)")
    print("19. Cosine (cos)")
    print("20. Tangent (tan)")
    print("21. View History")
    print("22. Clear History")
    print("23. Save History")
    print("==============================")

    choice = input("Choose an operation (1-23): ")

    if choice == "21":
        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)

        print("==============================")

    elif choice == "22":
        history.clear()
        print("\n==============================")
        print("History cleared successfully.")
        print("==============================")

    elif choice == "23":

        with open("history.txt", "w") as file:

            if len(history) == 0:
                file.write("No calculations yet.\n")

            else:
                for item in history:
                    file.write(item + "\n")

        print("\n==============================")
        print("History saved to history.txt")
        print("==============================")

    elif choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:

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

        if choice == "9":
            try:
                num = float(input("Enter a number: "))

                answer = num / 100

                print("Answer:", answer)

                history.append(f"{num}% = {answer}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "10":
            try:
                num = float(input("Enter a whole number: "))

                if num < 0:
                    print("Error: Factorial cannot be calculated for negative numbers.")

                elif num != int(num):
                    print("Error: Factorial only works with whole numbers.")

                else:
                    answer = math.factorial(int(num))

                    print("Answer:", answer)

                    history.append(f"{int(num)}! = {answer}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "11":
            try:
                num = float(input("Enter a number: "))

                if num >= 0:
                    answer = num ** (1 / 3)
                else:
                    answer = -((-num) ** (1 / 3))

                print("Answer:", answer)

                history.append(f"∛{num} = {answer}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "12":
            try:
                num = float(input("Enter a number: "))

                answer = abs(num)

                print("Answer:", answer)

                history.append(f"|{num}| = {answer}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "13":
            try:
                num = float(input("Enter a number: "))

                if num == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    answer = 1 / num

                    print("Answer:", answer)

                    history.append(f"1/{num} = {answer}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "14":
            answer = math.pi

            print("π =", answer)

            history.append(f"π = {answer}")

            continue

        if choice == "15":
            try:
                num = float(input("Enter a number: "))

                answer = math.e * num

                print("Answer:", answer)

                history.append(f"e × {num} = {answer}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "16":
            try:
                num = float(input("Enter a positive number: "))

                if num <= 0:
                    print("Error: Logarithm is only defined for numbers greater than zero.")
                else:
                    answer = math.log10(num)

                    print("Answer:", answer)

                    history.append(f"log({num}) = {answer}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "17":
            try:
                num = float(input("Enter a positive number: "))

                if num <= 0:
                    print("Error: Natural logarithm is only defined for numbers greater than zero.")
                else:
                    answer = math.log(num)

                    print("Answer:", round(answer, 10))

                    history.append(f"ln({num}) = {round(answer, 10)}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "18":
            try:
                angle = float(input("Enter an angle in degrees: "))

                answer = math.sin(math.radians(angle))

                print("Answer:", round(answer, 10))

                history.append(f"sin({angle}°) = {round(answer, 10)}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "19":
            try:
                angle = float(input("Enter an angle in degrees: "))

                answer = math.cos(math.radians(angle))

                print("Answer:", round(answer, 10))

                history.append(f"cos({angle}°) = {round(answer, 10)}")

            except ValueError:
                print("Invalid input.")

            continue

        if choice == "20":
            try:
                angle = float(input("Enter an angle in degrees: "))

                answer = math.tan(math.radians(angle))

                print("Answer:", round(answer, 10))

                history.append(f"tan({angle}°) = {round(answer, 10)}")

            except ValueError:
                print("Invalid input.")

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
