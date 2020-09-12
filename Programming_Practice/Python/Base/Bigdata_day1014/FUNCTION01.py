def PrintGugudan(dan):
    for i in range(9):
        print(f"{dan} * {i} = {dan * i}")
    print(f"{dan}단 출력 완료.")


if __name__ == "__main__":
    dan = int(input("단 입력 >> "))
    PrintGugudan(dan)
