# 구구단
import os

while True:
    dan = input("몇 단을 출력할지 : ")
    if dan.isalpha() or dan == '':
        os.system('cls')
    else:
        break
dan = int(dan)
for i in range(1, 10):
    print(f"{dan} * {i} = {dan * i}")

# k = 0
# ddan = int(input("몇 단을 출력할지 : "))
#
# while k < 10:
#     print(f"{ddan} * {k} = {ddan * k}")
#     k += 1