x = float(input("Enter first number "))
y = float(input("Enter second number "))
operator = input("Enter your action ")

if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    if y == 0:
        result = "You can not divide by 0 "
    else:
        result = x / y
else:
    result = "Not correct operator"

print(result)
