list_1 = [1, 2, 3, 54, 7, 97]

print(list_1)

if list_1:
    list_1.insert(0, list_1.pop())
    print(list_1)
else:
    print([])

