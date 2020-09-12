# global keyword
a = 20 # 전역변수

def func5():
    global a # 이 함수 안에서의 a 변수는 전역변수 a
    a = 10
    print(f"func5() a : {a}")

func5()
print(a)