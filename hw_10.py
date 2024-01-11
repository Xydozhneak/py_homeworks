while True:
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numeric values.")
        continue

    operator = input("Enter your action (+, -, *, /): ")
    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "*":
        result = x * y
    elif operator == "/":
        if y == 0:
            result = "You cannot divide by 0."
        else:
            result = x / y
    else:
        result = "Not a correct operator."

    print(result)

    repeat = input("Do you want to perform another calculation? (yes/no) ").lower()
    if repeat != "yes" and repeat != "y":
        break
