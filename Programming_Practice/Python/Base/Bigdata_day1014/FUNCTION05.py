# 사칙연산 함수
def inputValue():
    return int(input("Enter Input : "))


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def printValue(x, y):
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {sub(x, y)}")
    print(f"{x} * {y} = {mul(x, y)}")
    print(f"{x} / {y} = {div(x, y):.2f}")


if __name__ == "__main__":
    #a = int(input("Enter First Input : "))
    #b = int(input("Enter Second Input : "))
    a = inputValue()
    b = inputValue()
    printValue(a, b)
    #print(f"{a} + {b} = {add(a, b)}")
    #print(f"{a} - {b} = {sub(a, b)}")
    #print(f"{a} * {b} = {mul(a, b)}")
    #print(f"{a} / {b} = {div(a, b):.2f}")