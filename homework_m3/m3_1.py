# # m3_1_1 level 1
def precent(x, p, y):
    f = ((x / 100) * p) * y
    print(f'Вклад за {y} лет/год, будет не менее {f:.0f} рублей.')


def calculation():
    precent(
        x=float(input('Contribution: ')),
        p=float(input('Precent: ')),
        y=int(input('Years: '))
    )


calculation()


# m3_1_2 level 2
i = int(input('Start: '))
f = int(input('Stop: '))

while i <= f:
    print('for - как частный случай while')
    i += 1


# m3_1_3 level 3
def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


print(sum_of_digits(int(input('Enter num please: '))))
# Another example
print(sum(map(int,input('Enter num please: '))))
