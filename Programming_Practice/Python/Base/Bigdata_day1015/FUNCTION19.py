# 여러개 매개변수


def para_func(*param):
    result = 0
    for num in param:
        result += num
    return result


if __name__ == "__main__":
    sum = para_func(10, 20)
    print(f"매개변수가 2개인 함수 호출 -> {sum}")

    sum = para_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"매개변수가 10개인 함수 호출 -> {sum}")