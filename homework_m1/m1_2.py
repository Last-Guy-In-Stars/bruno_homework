import re
# Level 1


def coincided() -> int:
    x1: int = input('Num1: ')
    x2: int = input('Num2: ')
    x3: int = input('Num3: ')

    if x1 == x2 and x2 == x3:
        return 3
    elif x1 == x2 and x2 != x3:
        return 2
    elif x1 != x2 and x2 == x3:
        return 2
    elif x1 == x3 and x2 != x1:
        return 2
    else:
        return 0


value = coincided()
print(value)

# Level 2

x1 = int(input('x1:'))
y1 = int(input('y1:'))
x2 = int(input('x2:'))
y2 = int(input('y2:'))
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print('NO')

# Level 3

password: str = input('Enter the strong password'
                      'only 8 character and to keep letters up and bottom:')
while True:
    if (len(password) <= 8):
        print("Not a Valid Password ")
        continue
    elif not re.search("[a-z]", password):
        print("Not a Valid Password ")
        continue
    elif not re.search("[A-Z]", password):
        print("Not a Valid Password ")
        continue
    else:
        print("Valid Password")
        break
