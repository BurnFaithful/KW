# 문자열과 리스트 비교

aa = "Hello World"
bb = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

print(aa)
print(aa[6])
print(aa[0:4])
print(aa[4:])

str = input("문자열을 자유롭게 입력해보세요 >> ")
s = int(input("출력할 시작 범위 >> "))
e = int(input("출력할 끝 범위 >> "))

print(str[s - 1:e])