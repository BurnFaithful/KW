# 리스트에 인덱스 값 수정

scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]
print(scores)

scores[0] = 80
print(scores)

scores[1] = scores[0]
print(scores)

i = 2 #index
number = 100
scores[i] = 10
scores[i + 2] = 20
print(scores)

if i >= 0 and i < len(scores):
    scores[i] = number
print(scores)

scoresList = scores;

for element in scoresList:
    print(element)