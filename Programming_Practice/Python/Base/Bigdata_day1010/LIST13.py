# 학생 성적 입력

STUDENT = 5

scoresList = ([int(input("한 명의 학생 총점 : ")) for _ in range(STUDENT)])

scoreAvg = sum(scoresList) / len(scoresList)

highScoreStudent = 0
for i in scoresList:
    if i >= 80:
        highScoreStudent += 1

print(f"전체 평균은 {scoreAvg}점")
print(f"80점 이상의 학생 수는 {highScoreStudent}명")
