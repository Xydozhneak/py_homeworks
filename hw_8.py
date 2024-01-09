import random
el = random.randint(3, 10)
lst = [random.randint(1, 100) for i in range(el)]
new_lst = [lst[0], lst[2], lst[-2]]
print(lst, "->", new_lst)
