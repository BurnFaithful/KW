# 리스트 반환

def initList(tempList):
    for i in range(0, 100):
        tempList.append(i)
    return tempList


def sumList(tempList):
    sum = 0
    for i in tempList:
        sum += i
    return sum


if __name__ == "__main__":
    tempList = []

    tempList = initList(tempList)
    print(tempList)

    sum = sumList(tempList)
    print(tempList, sum)