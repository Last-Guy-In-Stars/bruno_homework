from random import randint

# m3_2 level 1
# list = [1, 4, 1, 6, "hello", "a", 5, "hello"]
# dup = [x for i, x in enumerate(list) if i != list.index(x)]

# m = []
# for i, x in enumerate(list):
#     if i != list.index(x):
#         m.append(x)

# print(list, dup, m, end="\n")

# m3_2 level 2
n = 5
m = [[[randint(0, 100)] for i in range(n)] for j in range(n)]

max_elem = m[0][0]
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] > max_elem:
            max_elem = m[i][j]

list_index_max = [(i, j) for i in range(len(m))
                  for j in range(len(m[i]))
                  if m[i][j] == max_elem]
line, column = list_index_max[0]
print('Максимальный элемент =', max_elem)
print('Строка =', line, 'Столбец =', column)
