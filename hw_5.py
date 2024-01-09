lst_1 = [0, 1, 7, 2, 4, 8]
lst_2 = [0]
lst_3 = [1, 3, 5]
lst_4 = [6]

a = lst_1[-1] if lst_1 else 0
sum_1 = sum(lst_1[i] for i in range(0, len(lst_1), 2))
result_1 = sum_1 * a
print(lst_1, "->", result_1)

a = lst_2[-1] if lst_2 else 0
sum_2 = sum(lst_2[i] for i in range(0, len(lst_2), 2))
result_2 = sum_2 * a
print(lst_2, "->", result_2)

a = lst_3[-1] if lst_3 else 0
sum_3 = sum(lst_3[i] for i in range(0, len(lst_3), 2))
result_3 = sum_3 * a
print(lst_3, "->", result_3)

a = lst_4[-1] if lst_4 else 0
sum_4 = sum(lst_4[i] for i in range(0, len(lst_4), 2))
result_4 = sum_4 * a
print(lst_4, "->", result_4)
