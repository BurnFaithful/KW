# 함수1 : parameter O, return value X
# 함수2 : parameter X, return value O
# 함수3 : parameter O, return value O
# 함수4 : parameter X, return value X

# 파이썬 함수 구성 : def 함수명(매개변수):
#                       return (variable, value, reference)


def func01(iValue, sName, fPI):
    print(iValue, sName, fPI)


def func02():
    sGrade = input("학점 입력 : ")
    return sGrade


def func03(fAvg):
    result = ''
    if fAvg >= 90:
        result = 'A'
    elif 80 <= fAvg <= 89:
        result = 'B'
    else:
        result = "C, D, F"
    return result


def func04():
    print("1. 새 게임")
    print("2. 게임 저장")
    print("3. 설정")
    print("4. 종료")

    select = int(input("선택 >> "))


if __name__ == "__main__":
    func01(100, 'Kwon', 3.14)
    sGrade = func02()
    score = float(input("평균 입력 : "))
    print(func03(score))