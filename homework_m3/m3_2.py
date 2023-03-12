# m3_2 level 1
list = [1, 4, 1, 6, "hello", "a", 5, "hello"]
dup = [x for i, x in enumerate(list) if i != list.index(x)]

m = []
for i, x in enumerate(list):
    if i != list.index(x):
        m.append(x)

print(list, end="\n")
print(dup)
print(m)

# m3_2 level 1
