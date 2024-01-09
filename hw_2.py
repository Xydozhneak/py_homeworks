x = int(input("Please enter a five digit number "))

first_digit, leftover = divmod(x, 10000)
second_digit, leftover = divmod(leftover, 1000)
third_digit, leftover = divmod(leftover, 100)
fourth_digit, leftover = divmod(leftover, 10)
fifth_digit, leftover = divmod(leftover, 1)

print(first_digit, second_digit, third_digit, fourth_digit, fifth_digit)
