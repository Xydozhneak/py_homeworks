import string

user_input = input("Enter 2 letters separated by '-' ")

min_char, max_char = user_input.split('-')

ascii_letters = string.ascii_letters

min_index = ascii_letters.index(min_char)
max_index = ascii_letters.index(max_char)

chars_between = ascii_letters[min_index:max_index + 1]

print(chars_between)
