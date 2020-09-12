heros = ["스파이더맨", "헐크", "캡틴마블", "아이언맨", "앤트맨", "토르", "배트맨"]

index = heros.index("배트맨")
heros.pop(index)
print(heros)

name = input("마블 영웅 이름 : ")
for i in heros:
    if heros.index(name):
        print(name, "찾았습니다.")
        break