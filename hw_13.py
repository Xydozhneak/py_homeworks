user_input = int(input("Enter number: "))

while user_input > 9:
    digits = [int(digit) for digit in str(user_input)]
    product = 1

    for digit in digits:
        product *= digit

    user_input = product

print(user_input)