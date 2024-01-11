import string
import keyword

users_variable = input("Enter the name of the variable: ")
is_valid_variable_name = True

for letter in users_variable:
    incorrect_letter = letter.isupper() or letter.isspace() or (letter in string.punctuation and letter != '_')
    if incorrect_letter:
        is_valid_variable_name = False
        break

if users_variable.isdigit() or users_variable[0].isdigit() or users_variable in keyword.kwlist:
    is_valid_variable_name = False

print(is_valid_variable_name)
