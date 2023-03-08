# Level 1

values: float = (5 + (7*5/8)) / 3**5

print(values)

# Level 2 Vasy Pupkin


def tag() -> int:
    len_mkad: int = 109
    v: int = 30
    t: int = 5
    return (v*t) % len_mkad


print(f'tag: {tag()}')


# Level 3

num_1: float = 124.2
num_2: int = -2
max: float = (num_1 > num_2) * num_1 or (num_2 >= num_1) * num_2
print('Max value:', max)

num_1: float = -9.3
num_2: float = -163.5
max: float = (num_1 > num_2) * num_1 or (num_2 >= num_1) * num_2
print('Max value:', max)
