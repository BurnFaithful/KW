# 현재 시간을 입력받아 6시간 전 시간을 알려줌

curtime = int(input("지금 몇시인가요? "))
print(f"현재 시간: {curtime}시")
prevtime = curtime - 6
if prevtime < 0:
    prevtime += 24
print(f"이전 시간: {prevtime}시")