list_1 = [1, 2, 3, 4, 5, 6]
mid_1 = len(list_1) // 2
resul_1 = list_1[:mid_1 + len(list_1) % 2]
resul_2 = list_1[mid_1 + len(list_1) % 2:]
print(resul_1, resul_2)

