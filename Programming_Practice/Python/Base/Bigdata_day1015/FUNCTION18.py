def initList(eList, oList):
    for i in range(1, 101, 2):
        oList.append(i)
    for i in range(0, 101, 2):
        eList.append(i)

    return eList, oList


if __name__ == "__main__":
    eList, oList = [], []

    eList, oList = initList(eList, oList)
    print(eList)
    print(oList)