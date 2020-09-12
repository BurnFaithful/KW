# 문자열 판단

userID = "qwer1234"
userPW = "1234567890"
inID = input("사용자 ID 입력 : ")
inPW = input("사용자 PW 입력 : ")

if inID == userID and inPW == userPW:
    print("아이디가 일치합니다. ", inID)
    print("패스워드가 일치합니다. ", inPW)
else:
    print("아이디 또는 패스워드가 불일치합니다.")

if inID == userID:
    if inPW == userPW:
        print("아이디 패스워드 모두 일치")
    else:
        print("패스워드 불일치")
else:
    print("아이디가 불일치")