# 문자열 반대로 출력

inStr = ""
outStr = ""
count = 0

inStr = input("문자열을 입력하시오: ")
count = len(inStr)

for i in range(0, count):
    outStr += inStr[count - (i + 1)]
print(outStr)

# print(inStr[::-1])