# 팩토리얼

factorial = 1

x = int(input("팩토리얼 구할 수 : "))

for i in range(x, 0, -1):
    if i == 1: print(f"{i}=", end='')
    else: print(f"{i}*", end='')
    factorial *= i
print(factorial)