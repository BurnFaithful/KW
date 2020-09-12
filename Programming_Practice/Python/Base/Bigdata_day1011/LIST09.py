def createNode():
    newNode = []
    return newNode

def newstudent(studentList):
    newNode = createNode()

    name = input("이름 >> ")
    newNode.append(name)

    cnt = int(input("입력할 점수 개수 >> "))
    for i in range(cnt):
        score = int(input(f"{i + 1}번 점수 >> "))
        newNode.append(score)

    return studentList.append(newNode)

def main():
    studentList = list()

    while True:
        newstudent(studentList)

        tot, avg = 0, 0

        for student in studentList:
            tot = sum(student[1:])
            avg = tot / len(student) - 1
            student.extend([tot, round(avg, 1)])

        ending = input("\n계속 입력(y/n)? ")
        if ending is "Y" or ending is "y": continue
        elif ending is "N" or ending is "n": break
        else: continue

    print("이름 점수1 점수2 총점 평균...")
    for i in studentList:
        print(" ".join(map(str, i)))

if __name__ == "__main__":
    main()