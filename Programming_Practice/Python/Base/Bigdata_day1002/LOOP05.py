num = int(input("출력할 별 수 입력>> "))

for i in range(1, num + 1):
    for j in range(i):
        print("*", end='')
    print()

for i in range(num, 0, -1):
    for j in range(i):
        print("*", end='')
    print()

for i in range(1, num + 1):
    for j in range(num - i):
        print(' ', end='')
    for k in range(i):
        print("*", end='')
    print()

for i in range(1, num + 1):
    for j in range(num - i):
        print(' ', end='')
    for k in range(i * 2 - 1):
        print("*", end='')
    print()

for i in range(1, num // 2 + 2):
    for j in range(1, num - i - 1):
        print(' ', end='')
    for k in range(i * 2 - 1):
        print("*", end='')
    print()
for i in range(num // 2, 0, -1):
    for j in range(1, num - i - 1):
        print(' ', end='')
    for k in range(i * 2 - 1):
        print("*", end='')
    print()