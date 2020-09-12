import os
import pymysql
import itertools
import logging
from contextlib import contextmanager
from Bigdata_day1017.memberQuery import *

# 회원 정보 : 번호 / ID / 비밀번호 / 이름 / 성별 / 나이
# DB Schema Definition
# 번호 (idx) : INTEGER(11) - Primary Key, NOT NULL, AUTO_INCREMENT
# ID (ID) : VARCHAR(20)
# 비밀번호 (password) : VARCHAR(20)
# 이름 (name) : VARCHAR(20)
# 성별 (sex) : VARCHAR(20)
# 나이 (age) : INTEGER(11)


@contextmanager
def dbConnect(cursAttr=pymysql.cursors.Cursor, dbHost='localhost', dbUser='root', dbPw='cout49!', dbName='KW', dbCharset='utf8'):
    conn = None
    try:
        conn = pymysql.connect(host=dbHost, user=dbUser, password=dbPw, db=dbName, charset=dbCharset)
        curs = conn.cursor(cursAttr)
        yield curs
        conn.commit()
    except pymysql.MySQLError as e:
        conn.rollback()
        logging.error(e)
    finally:
        conn.close()


def menuDisplay():
    print()
    print()
    print("0. 초기 생성 / 1. 멤버 추가 / 2. 멤버 리스트 / 3. 멤버 찾기 / 4. 정보 수정 / 5. 정보 삭제 / 6. 화면 지우기 / 7. 종료")


def initMember():
    with dbConnect(pymysql.cursors.DictCursor) as curs:
        curs.execute(queryMemberGetLastIndex)
        lastIndex = curs.fetchone()['idx']

        initInfo = [lastIndex + 1, "Youngmin", "1234", "권영민", "남자", 26]
        curs.execute(queryMemberInit, initInfo)


def addMember():
    with dbConnect() as curs:
        curs.execute(queryMemberGetColumnsNameNotInIndex)
        columnNames = curs.fetchall()

        memberInfo = list()
        columnNames = itertools.chain(*columnNames)
        for columName in columnNames:
            memberInfo.append(input(f"-> {columName} : "))

        curs.execute(queryMemberAdd, memberInfo)


def printMemberList():
    with dbConnect() as curs:
        curs.execute(queryMemberGetColumnsName)
        columnNames = curs.fetchall()

        print(f"{'':<10}".join(itertools.chain(*columnNames)))

        curs.execute(queryMemberAllSelect)
        rows = curs.fetchall()

        if rows:
            print("------------------------------------회원 리스트------------------------------------")
            for row in rows:
                print(f"{'':<10}".join(map(str, row)))
        else:
            print("회원이 아무도 없습니다.")


def researchMember():
    modifyCommand = int(input("찾고자 하는 정보(1. ID / 2. 이름 / 3. 성별 / 4. 나이) : "))
    whereColumnName = ""
    if modifyCommand == 1:
        whereColumnName = "ID"
    elif modifyCommand == 2:
        whereColumnName = "name"
    elif modifyCommand == 3:
        whereColumnName = "age"
    researchInfo = input(f"찾고자 하는 {whereColumnName} : ")

    with dbConnect() as curs:
        curs.execute(queryMemberResearchSpecificColumn, (whereColumnName.strip("\'"), researchInfo))
        rows = curs.fetchall()

        if rows:
            for row in rows:
                print('\t'.join(map(str, row)))
        else:
            print("해당하는 이름의 회원이 없습니다.")


def modifyMemberInfo():
    modifyCommand = int(input("수정하고자 하는 정보(1. 비밀번호 / 2. 이름 / 3. 나이) : "))
    whereColumnName = ""
    if modifyCommand == 1:
        whereColumnName = "password"
    elif modifyCommand == 2:
        whereColumnName = "name"
    elif modifyCommand == 3:
        whereColumnName = "age"
    destInfo = input(f"수정할 {whereColumnName} : ")

    with dbConnect() as curs:
        curs.execute(queryMemberOneResearchSpecificColumn, (whereColumnName, destInfo))
        # curs.execute(queryMemberOneResearch, (destName,))
        researchRow = curs.fetchall()
        if researchRow:
            modifyInfo = input(f"{whereColumnName} 내용 수정 : ")
            count = curs.execute(queryMemberModifySpecificColumn, (whereColumnName, modifyInfo, whereColumnName, modifyInfo))
            # count = curs.execute(queryMemberMultiModify, (*modifyInfo, destName))s
            # count = curs.execute(queryMemberModify, (modifyName, destName))
            print(f"{count}개 변경 완료.")
        else:
            print("해당하는 이름의 회원이 없습니다.")


def removeMember():
    removeCommand = int(input("삭제하고자 하는 정보(1. 이름 / 2. 나이) : "))
    whereColumnName = ""
    if removeCommand == 1:
        whereColumnName = "name"
    elif removeCommand == 2:
        whereColumnName = "age"
    destInfo = input(f"삭제하고자 하는 {whereColumnName} : ")

    with dbConnect() as curs:
        curs.execute(queryMemberOneResearchSpecificColumn, (whereColumnName, destInfo))
        researchRow = curs.fetchall()
        if researchRow:
            deleteConfirm = input("정말 삭제하시겠습니까?(Y/N)")
            if deleteConfirm is 'Y' or deleteConfirm is 'y':
                count = curs.execute(queryMemberRemoveSpecificColumn, (whereColumnName, destInfo))
                print(f"{count} 개 삭제 완료.")
        else:
            print("해당하는 이름의 회원이 없습니다.")


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


def exitProgram():
    print("프로그램을 종료합니다.")
    os._exit(0)


def main():
    print("### 간단한 회원 관리 프로그램 ###")
    while True:
        menuDisplay()
        command = inputFilter(0, 7)

        if command == 0:
            initMember()
        elif command == 1:
            addMember()
        elif command == 2:
            printMemberList()
        elif command == 3:
            researchMember()
        elif command == 4:
            modifyMemberInfo()
        elif command == 5:
            removeMember()
        elif command == 6:
            screenClear()
        elif command == 7:
            exitProgram()


if __name__ == "__main__":
    main()