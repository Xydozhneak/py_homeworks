lst_1 = [0, 1, 0, 0, 0, 12, 3]

new_lst_1 = [el for el in lst_1 if el != 0]
print(new_lst_1)

quantity = len(lst_1) - len(new_lst_1)

new_lst_1 += [0 for _ in range(quantity)]
print(lst_1, "->", new_lst_1)
