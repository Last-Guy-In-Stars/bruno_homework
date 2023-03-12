# m3_1_1
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
