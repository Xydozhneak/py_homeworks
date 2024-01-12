def common_elements():
    multiples_of_3 = [i for i in range(1, 200) if i % 3 == 0]
    multiples_of_5 = [i for i in range(1, 100) if i % 5 == 0]

    common_set = set(multiples_of_3) & set(multiples_of_5)

    return common_set


result = common_elements()

print(result)
