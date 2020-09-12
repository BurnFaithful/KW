def aaa():
    print("AAA함수 시작")
    ccc()
    ddd()
    print("AAA함수 끝")

def bbb():
    print("BBB함수 시작")
    print("BBB함수 끝")

def ccc():
    print("CCC함수 시작")
    print("CCC함수 끝")

def ddd():
    print("DDD함수 시작")
    bbb()
    print("DDD함수 끝")

def main():
    print("메인함수 시작")
    aaa()
    print("메인함수 끝")

main()

# 메인 시작
# A 시작
# C 시작
# C 끝
# D 시작
# B 시작
# B 끝
# D 끝
# A 끝
# 메인 끝