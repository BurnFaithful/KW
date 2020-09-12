# 문자열 중에서 가운데 글자 찾기
str = input("문자열을 입력하세요: ")

length = len(str)
print(length, "개")

if length % 2 == 1:
    ch1 = str[length // 2]
    print("가운데 글자는", ch1)
else:
    ch1 = str[(length // 2) - 1]
    ch2 = str[length // 2]
    print("가운데 글자는", ch1, ch2)