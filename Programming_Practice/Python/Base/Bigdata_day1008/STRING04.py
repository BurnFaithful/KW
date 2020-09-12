# 문자열의 모든 글자 뒤에 $를 붙여서 출력

ss = "파이썬 굿!"

sslen = len(ss)

for i in ss:
    print(i + '$', end='')
print()

print('$'.join(ss) + '$')