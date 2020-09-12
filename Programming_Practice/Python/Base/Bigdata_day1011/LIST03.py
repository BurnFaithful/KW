# 문자열 길이를 이용한 출력
letter = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
print(letter)

length = len(letter)
for i in range(length):
    print(letter[i], end=' ')

print(' '.join(letter))

shopping = []
shopping.append("두부")
shopping.append("양배추")