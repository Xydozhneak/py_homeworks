def pow_func(x):
    return x ** 2


def some_gen(begin, end, func):
    current_value = begin
    count = 0

    while count < end:
        yield current_value
        current_value = func(current_value)
        count += 1


gen = some_gen(2, 4, pow_func)

print(list(gen))
