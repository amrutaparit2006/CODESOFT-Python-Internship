44def calculator():
    print("===== SIMPLE CALCULATOR =====")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number.")
        return

    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    elif choice == "5":
        if num2 == 0:
            print("Cannot use modulus with zero.")
            return
        result = num1 % num2
    else:
        print("Invalid operation.")
        return

    print("Result =", result)

calculator()
