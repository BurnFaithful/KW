# 입력된 나이에 10년 후의 나이 계산

name = input("당신의 이름은 무엇? ")
print("{}님 반갑습니다.".format(name))

age = input("How old are you? ") # 문자형 숫자
print("10년 후 당신의 나이는 {}세 입니다.".format(int(age) + 10))