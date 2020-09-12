import os # 파이썬이 OS의 일부 기능 가져옴

while True:
    s1 = input("number input plz...>> ")

    if s1.isalpha() or s1 == '':
        os.system('cls')
    else:
        break

s1 = int(s1)
print(f"{s1} + {10} = {s1 + 10}")