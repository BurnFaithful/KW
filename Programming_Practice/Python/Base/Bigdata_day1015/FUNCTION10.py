def func1():
    a = 10 # func1()에서만 적용되는 local variable
    print(f"func1() a : {a}")
    a = 10 + 20
    print(f"func1() a : {a}")

def func2():
    print(f"func2() a : {a}") # a 변수가 선언되어 있지 않기 때문

a = 100 # 전역변수 - 파일 전체에 적용되는 변수

func1()
func2()