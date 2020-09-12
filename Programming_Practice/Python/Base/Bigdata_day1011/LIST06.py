heros = ["스파이더맨", "헐크", "캡틴마블", "아이언맨", "앤트맨", "토르", "배트맨"]

srhName = input("찾을 영웅 이름: ")
for i in heros:
    if i == srhName:
        print("찾음")
        break
    else:
        print("없음")

delName = input("삭제할 이름: ")
for i in heros:
    if heros.index(delName):
        heros.remove(delName)
print(heros)