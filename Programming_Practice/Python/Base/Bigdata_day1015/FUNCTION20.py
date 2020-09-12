import random

def getNumber():
    return random.randrange(1, 46)


if __name__ == "__main__":
    lotto = []
    num = 0
    print("=== 로또 추첨을 시작합니다. ===")

    for i in range(10):
        lotto.clear()
        while True:
            num = getNumber()

            if lotto.count(num) == 0:
                lotto.append(num)

            if len(lotto) >= 6: break

        print("추천 로또 번호 -> ", end='')
        lotto.sort()
        for i in lotto:
            print(f"{i}", end=' ')
        print()