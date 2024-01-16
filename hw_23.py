from inspect import isgenerator


def prime_generator(end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    current_num = 2

    while current_num <= end:
        if is_prime(current_num):
            yield current_num
        current_num += 1


gen = prime_generator(1)

assert isgenerator(gen) == True, 'Test0'

print(list(prime_generator(21)))
print('OK')
