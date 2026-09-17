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
    print("24. Average")
    print("25. Minimum Value")
    print("26. Maximum Value")
    print("27. Percentage Increase")
    print("28. Percentage Decrease")
    print("29. GCD (Greatest Common Divisor)")
    print("30. LCM (Least Common Multiple)")
    print("31. Permutation (nPr)")
    print("32. Combination (nCr)")
    print("33. Round Number")
    print("==============================")

    choice = input("Choose an operation (1-33): ")
    # View History
    if choice == "21":
        if len(history) == 0:
            print("No calculations yet.")
        else:
            print("\nCalculation History:")
            for item in history:
                print(item)
        print("==============================")
    # Clear History
    elif choice == "22":
        history.clear()
        print("\n==============================")
        print("History cleared successfully.")
        print("==============================")
    # Save History
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
    # Average
    elif choice == "24":
        try:
            numbers = input(
                "Enter numbers separated by spaces: "
            ).split()
            if len(numbers) == 0:
                print("No numbers entered.")
            else:
                numbers = [float(num) for num in numbers]
                answer = sum(numbers) / len(numbers)
                print("Average:", answer)
                history.append(
                    f"Average of {numbers} = {answer}"
                )

        except ValueError:
            print("Invalid input. Please enter numbers only.")
    # Minimum Value
    elif choice == "25":
        try:
            numbers = input(
                "Enter numbers separated by spaces: "
            ).split()

            if len(numbers) == 0:
                print("No numbers entered.")
            else:
                numbers = [float(num) for num in numbers]
                answer = min(numbers)
                print("Minimum value:", answer)
                history.append(
                    f"Minimum of {numbers} = {answer}"
                )
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    # Maximum Value
    elif choice == "26":
        try:
            numbers = input(
                "Enter numbers separated by spaces: "
            ).split()
            
            if len(numbers) == 0:
                print("No numbers entered.")
            else:
                numbers = [float(num) for num in numbers]
                answer = max(numbers)
                print("Maximum value:", answer)
                history.append(
                    f"Maximum of {numbers} = {answer}"
                )
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    # Percentage Increase
    elif choice == "27":
        try:
            original = float(
                input("Enter the original value: ")
            )
            new_value = float(
                input("Enter the new value: ")
            )
            if original == 0:
                print(
                    "Error: Original value cannot be zero."
                )
            else:
                answer = (
                    (new_value - original) / original
                ) * 100
                print(
                    "Percentage increase:",
                    answer,
                    "%"
                )
                history.append(
                    f"Percentage increase from "
                    f"{original} to {new_value} = "
                    f"{answer}%"
                )
        except ValueError:
            print("Invalid input.")
    # Percentage Decrease
    elif choice == "28":
        try:
            original = float(
                input("Enter the original value: ")
            )
            new_value = float(
                input("Enter the new value: ")
            )
            if original == 0:
                print(
                    "Error: Original value cannot be zero."
                )
            else:
                answer = (
                    (original - new_value) / original
                ) * 100
                print(
                    "Percentage decrease:",
                    answer,
                    "%"
                )
                history.append(
                    f"Percentage decrease from "
                    f"{original} to {new_value} = "
                    f"{answer}%"
                )
        except ValueError:
            print("Invalid input.")
    # GCD
    elif choice == "29":
        try:
            num1 = int(
                input("Enter the first whole number: ")
            )
            num2 = int(
                input("Enter the second whole number: ")
            )
            answer = math.gcd(num1, num2)
            print("GCD:", answer)
            history.append(
                f"GCD({num1}, {num2}) = {answer}"
            )
        except ValueError:
            print(
                "Invalid input. Please enter whole numbers."
            )
    # LCM
    elif choice == "30":
        try:
            num1 = int(
                input("Enter the first whole number: ")
            )
            num2 = int(
                input("Enter the second whole number: ")
            )
            if num1 == 0 or num2 == 0:
                answer = 0
            else:
                answer = math.lcm(num1, num2)

            print("LCM:", answer)

            history.append(
                f"LCM({num1}, {num2}) = {answer}"
            )
        except ValueError:
            print(
                "Invalid input. Please enter whole numbers."
            )
    # Permutation
    elif choice == "31":
        try:
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))

            if n < 0 or r < 0:
                print(
                    "Error: Values cannot be negative."
                )
            elif r > n:
                print(
                    "Error: r cannot be greater than n."
                )
            else:
                answer = math.perm(n, r)
                print("Permutation:", answer)
                history.append(
                    f"{n}P{r} = {answer}"
                )
        except ValueError:
            print(
                "Invalid input. Please enter whole numbers."
            )
    # Combination
    elif choice == "32":
        try:
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))

            if n < 0 or r < 0:
                print(
                    "Error: Values cannot be negative."
                )
            elif r > n:
                print(
                    "Error: r cannot be greater than n."
                )
            else:
                answer = math.comb(n, r)
                print("Combination:", answer)
                history.append(
                    f"{n}C{r} = {answer}"
                )
        except ValueError:
            print(
                "Invalid input. Please enter whole numbers."
            )
    # Round Number
    elif choice == "33":
        try:
            num = float(
                input("Enter a number: ")
            )
            decimal_places = int(
                input("Enter number of decimal places: ")
            )
            if decimal_places < 0:
                print(
                    "Error: Decimal places cannot be negative."
                )
            else:
                answer = round(
                    num,
                    decimal_places
                )
                print(
                    "Rounded number:",
                    answer
                )
                history.append(
                    f"Round({num}, {decimal_places}) = "
                    f"{answer}"
                )
        except ValueError:
            print("Invalid input.")
    # Original Calculator Functions
    elif choice in [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11", "12", "13", "14",
        "15", "16", "17", "18",
        "19", "20"
    ]:
        # Square Root
        if choice == "8":
            try:
                num = float(
                    input("Enter a number: ")
                )
                if num < 0:
                    print(
                        "Error: Cannot find the square "
                        "root of a negative number."
                    )
                else:
                    answer = math.sqrt(num)
                    print("Answer:", answer)
                    history.append(
                        f"√{num} = {answer}"
                    )
            except ValueError:
                print(
                    "\n=============================="
                )
                print(
                    "Invalid input. Please enter a number."
                )
                print(
                    "=============================="
                )
            continue
        # Percentage
        if choice == "9":
            try:
                num = float(
                    input("Enter a number: ")
                )
                answer = num / 100
                print("Answer:", answer)
                history.append(
                    f"{num}% = {answer}"
                )
            except ValueError:
                print("Invalid input.")
            continue
        # Factorial
        if choice == "10":
            try:
                num = float(
                    input("Enter a whole number: ")
                )
                if num < 0:
                    print(
                        "Error: Factorial cannot be "
                        "calculated for negative numbers."
                    )
                elif num != int(num):
                    print(
                        "Error: Factorial only works "
                        "with whole numbers."
                    )
                else:
                    answer = math.factorial(
                        int(num)
                    )
                    print("Answer:", answer)

                    history.append(
                        f"{int(num)}! = {answer}"
                    )
            except ValueError:
                print("Invalid input.")
            continue
        # Cube Root
        if choice == "11":
            try:
                num = float(
                    input("Enter a number: ")
                )
                if num >= 0:
                    answer = num ** (1 / 3)
                else:
                    answer = -((-num) ** (1 / 3))
                print("Answer:", answer)
                history.append(
                    f"∛{num} = {answer}"
                )
            except ValueError:
                print("Invalid input.")
            continue
        # Absolute Value
        if choice == "12":
            try:
                num = float(
                    input("Enter a number: ")
                )
                answer = abs(num)
                print("Answer:", answer)
                history.append(
                    f"|{num}| = {answer}"
                )
            except ValueError:
                print("Invalid input.")
            continue
        # Reciprocal
        if choice == "13":
            try:
                num = float(
                    input("Enter a number: ")
                )
                if num == 0:
                    print(
                        "Error: Cannot divide by zero."
                    )
                else:
                    answer = 1 / num
                    print("Answer:", answer)
                    history.append(
                        f"1/{num} = {answer}"
                    )
            except ValueError:
                print("Invalid input.")
            continue
        # Pi
        if choice == "14":
            answer = math.pi
            print("π =", answer)
            history.append(
                f"π = {answer}"
            )
            continue
        # Euler's Number
        if choice == "15":
            try:
                num = float(
                    input("Enter a number: ")
                )
                answer = math.e * num
                print("Answer:", answer)
                history.append(
                    f"e × {num} = {answer}"
                )
            except ValueError:
                print("Invalid input.")
            continue
        # Logarithm
        if choice == "16":
            try:
                num = float(
                    input("Enter a positive number: ")
                )
                if num <= 0:
                    print(
                        "Error: Logarithm is only defined "
                        "for numbers greater than zero."
                    )
                else:
                    answer = math.log10(num)
                    print("Answer:", answer)
                    history.append(
                        f"log({num}) = {answer}"
                    )
            except ValueError:
                print("Invalid input.")
            continue
        # Natural Logarithm
        if choice == "17":
            try:
                num = float(
                    input("Enter a positive number: ")
                )
                if num <= 0:
                    print(
                        "Error: Natural logarithm is "
                        "only defined for numbers "
                        "greater than zero."
                    )
                else:
                    answer = math.log(num)
                    answer = round(
                        answer,
                        10
                    )
                    print("Answer:", answer)

                    history.append(
                        f"ln({num}) = {answer}"
                    )
            except ValueError:
                print("Invalid input.")
            continue
        # Sine
        if choice == "18":
            try:
                angle = float(
                    input(
                        "Enter an angle in degrees: "
                    )
                )
                answer = math.sin(
                    math.radians(angle)
                )
                answer = round(
                    answer,
                    10
                )
                print("Answer:", answer)
                history.append(
                    f"sin({angle}°) = {answer}"
                )
            except ValueError:
                print("Invalid input.")
            continue
        # Cosine
        if choice == "19":
            try:
                angle = float(
                    input(
                        "Enter an angle in degrees: "
                    )
                )
                answer = math.cos(
                    math.radians(angle)
                )
                answer = round(
                    answer,
                    10
                )
                print("Answer:", answer)
                history.append(
                    f"cos({angle}°) = {answer}"
                )
            except ValueError:
                print("Invalid input.")
            continue
        # Tangent
        if choice == "20":
            try:
                angle = float(
                    input(
                        "Enter an angle in degrees: "
                    )
                )
                answer = math.tan(
                    math.radians(angle)
                )
                answer = round(
                    answer,
                    10
                )
                print("Answer:", answer)

                history.append(
                    f"tan({angle}°) = {answer}"
                )
            except ValueError:
                print("Invalid input.")
            continue
        # Addition, Subtraction, Multiplication,
        # Division, Exponent, Modulus, Floor Division
        try:
            num1 = float(
                input("Enter the first value: ")
            )

            num2 = float(
                input("Enter the second value: ")
            )
        except ValueError:
            print(
                "\n=============================="
            )
            print(
                "Invalid input. Please enter numbers only."
            )
            print(
                "=============================="
            )
            continue
        # Addition
        if choice == "1":
            answer = num1 + num2
            print("Answer:", answer)
            history.append(
                f"{num1} + {num2} = {answer}"
            )
        # Subtraction
        elif choice == "2":
            answer = num1 - num2
            print("Answer:", answer)
            history.append(
                f"{num1} - {num2} = {answer}"
            )
        # Multiplication
        elif choice == "3":
            answer = num1 * num2
            print("Answer:", answer)
            history.append(
                f"{num1} × {num2} = {answer}"
            )
        # Division
        elif choice == "4":
            if num2 == 0:
                print(
                    "Error: Cannot divide by zero."
                )
            else:
                answer = num1 / num2
                print("Answer:", answer)
                history.append(
                    f"{num1} ÷ {num2} = {answer}"
                )
        # Exponent
        elif choice == "5":
            answer = num1 ** num2
            print("Answer:", answer)
            history.append(
                f"{num1} ^ {num2} = {answer}"
            )
        # Modulus
        elif choice == "6":
            if num2 == 0:
                print(
                    "Error: Cannot divide by zero."
                )
            else:
                answer = num1 % num2
                print("Answer:", answer)
                history.append(
                    f"{num1} % {num2} = {answer}"
                )
        # Floor Division
        elif choice == "7":
            if num2 == 0:
                print(
                    "Error: Cannot divide by zero."
                )
            else:
                answer = num1 // num2
                print("Answer:", answer)
                history.append(
                    f"{num1} // {num2} = {answer}"
                )
    # Invalid Choice
    else:
        print("Invalid operation.")
    again = input(
        "\nDo you want to perform another calculation? "
        "(yes/no): "
    ).lower()
    if again != "yes":
        print("Program Ended.")
        break
