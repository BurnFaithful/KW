scores = []

for i in range(10):
    jumsu = int(input("과목 점수를 입력 : "))
    scores.append(jumsu)

a = sum(scores)
print(scores)
print(a)