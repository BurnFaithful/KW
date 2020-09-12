# 특정 입력 받아서 리스트에 저장, 종료시 엔터키 입력

marvelNameList = list()

while True:
    name = input("마블 히어로 이름 >> ")
    if name is "": break
    marvelNameList.append(name)

print(f"마블 영웅 리스트 : {','.join(marvelNameList)}")