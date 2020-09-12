import winsound

print("369 게임 시작")

n = 1
while n <= 50:
    if n % 3 == 0 or "3" in str(n):
        print("박수")
        winsound.Beep(500, 300)
    else:
        print(n)
    n += 1

print("게임 끝.")