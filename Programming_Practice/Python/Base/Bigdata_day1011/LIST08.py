studentList = []
studentList.append([100, 95, 82])
studentList.append([87, 91, 76])
studentList.append([62, 100, 83])

# for i in range(3):
#     print(f"---{i + 1}번째 사람의 점수---")
#     listval = []
#     for j in range(3):
#         val = int(input("과목 점수 입력 : "))
#         listval.append(val)
#     studentList.append(listval)
#
print(studentList)

for stu in studentList:
    tot = 0

    for score in stu:
        tot += score

    avg = tot / len(stu)
    stu.append(tot)
    stu.append(round(avg))

    if 90 <= avg <= 100: stu.append("A")
    elif 80 <= avg <= 89: stu.append("B")
    elif 70 <= avg <= 79: stu.append("C")
    elif 60 <= avg <= 69: stu.append("D")
    else: stu.append("F")

print("==== 최종 성적 리스트 ====")
print("번호\t 점수1 \t 점수2\t 점수3\t 총점\t 평균\t 학점\t")
for index, i in enumerate(studentList):
    print(f"{index}\t".ljust(7) + (f"\t".center(4)).join(map(str, i)))

# studentList = [[sum(i), sum(i) / len(i)] for i in studentList]
# extendlist = [studentList[index].extend(j) for index, j in enumerate([[sum(i), sum(i) / len(i)] for i in studentList])]
# print(studentList)
