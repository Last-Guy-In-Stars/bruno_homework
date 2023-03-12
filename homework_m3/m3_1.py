# # m3_1_1 level 1
# def precent(x, p, y):
#     f = ((x / 100) * p) * y
#     print(f'Вклад за {y} лет/год, будет не менее {f:.0f} рублей.')


# def calculation():
#     precent(
#         x=float(input('Contribution: ')),
#         p=float(input('Precent: ')),
#         y=int(input('Years: '))
#     )


# calculation()


# m3_1_2 level 2

i = int(input('Start: '))
f = int(input('Stop: '))

while i <= f:
    print('for - как частный случай while')
    i += 1
