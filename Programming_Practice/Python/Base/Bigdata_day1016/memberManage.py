import os
import sys

# 회원 정보 : 번호 / ID / 비밀번호 / 이름 / 성별 / 나이 / 직급 / 회사명 / 회사주소 / 우편번호 / 회사전화번호 / 휴대폰번호

INDEX, ID, PW, NAME, SEX, AGE = 0, 1, 2, 3, 4, 5


index = 1

def menuDisplay():
    print()
    print()
    print("0. 초기 생성 / 1. 멤버 추가 / 2. 멤버 리스트 / 3. 멤버 찾기 / 4. 정보 수정 / 5. 정보 삭제 / 6. 화면 지우기 / 7. 종료")


def initList(memberList):
    global index
    initInfo = [index, "Youngmin", "1234", "권영민", "남자", 26]
    index += 1

    memberList.append(initInfo)

def addMember(memberList):
    columnHeadList = ["아이디", "패스워드", "이름", "성별", "나이"]

    memberInfo = list()
    global index
    index += 1
    memberInfo.append(index)
    for i in columnHeadList:
        memberInfo.append(input(f"-> {i} : "))

    memberList.append(memberInfo)


def printMemberList(memberList):
    columnHeadList = ["번호", "ID", "비밀번호", "이름", "성별", "나이"]
    if len(memberList) > 0:
        print(f"{'':<10}".join(columnHeadList))
        for i in memberList:
            print(f"{'':<10}".join(map(str, i)))
    else:
        print("회원이 아무도 없습니다.")


def findMember(memberList, name):
    findMemberList = list()
    for i in memberList:
        if i[3] in name:
            findMemberList.append(i)

    return findMemberList


def findMemberCount(memberList, name):
    count = 0
    for i in memberList:
        if i[NAME] in name:
            count += 1

    return count


def researchMember(memberList):
    researchName = input("찾고자 하는 이름 : ")

    findMemberList = findMember(memberList, researchName)
    for i in findMemberList:
        print('\t'.join(map(str, i)))


def modifyMemberInfo(memberList):
    destName = input("수정하고자 하는 이름 : ")

    findCount = findMemberCount(memberList, destName)
    if findCount > 0:
        print(f"수정 전 : {destName}")
        modifyName = input("수정할 이름 : ")
        for i in memberList:
            if i[NAME] in destName:
                i[NAME] = modifyName
        print(f" {findCount}개 변경 완료.")
    else:
        print("수정할 이름이 목록에 없습니다.")


def removeMember(memberList):
    destName = input("삭제하고자 하는 이름 : ")

    findCount = findMemberCount(memberList, destName)
    if findCount > 0:
        memberIndex = 0
        while memberIndex < len(memberList):
            if memberList[memberIndex][NAME] in destName:
                print(f"목록의 {memberList[memberIndex][INDEX]}번 회원 삭제.")
                del(memberList[memberIndex])
                memberIndex -= 1
            memberIndex += 1
        print(f"{findCount} 개 목록 삭제 완료.")
    else:
        print("삭제할 이름이 목록에 없습니다.")


def screenClear():
    os.system("cls")


def inputFilter(min, max):
    isError = True
    while True:
        command = input("->")

        try:
            command = int(command)
            if command >= min and command <= max:
                isError = False
                break
            else:
                print(f"{min}부터 {max} 사이로 입력.")
        except ValueError:
            print("잘못된 입력")

        if isError is True:
            menuDisplay()

    return command


def main():
    memberList = list()

    print("### 간단한 회원 관리 프로그램")
    while True:
        menuDisplay()
        command = inputFilter(0, 7)

        if command == 0:
            initList(memberList)
        elif command == 1:
            addMember(memberList)
        elif command == 2:
            printMemberList(memberList)
        elif command == 3:
            researchMember(memberList)
        elif command == 4:
            modifyMemberInfo(memberList)
        elif command == 5:
            removeMember(memberList)
        elif command == 6:
            screenClear()
        elif command == 7:
            os._exit(0)


if __name__ == "__main__":
    main()