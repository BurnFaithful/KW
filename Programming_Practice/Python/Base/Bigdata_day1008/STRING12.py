# 문자열 중간의 공백까지 삭제

inStr = "    한 글 Python 프로 그래 밍   "
outStr = ""

# for i in inStr:
#     if i != ' ':
#         outStr += inStr[i]

outStr = inStr.replace(' ', '')
print(f"원래 문자열 : {inStr}")
print(f"공백제거 문자열 : {outStr}")