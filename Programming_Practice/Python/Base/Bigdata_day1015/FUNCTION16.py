# 리스트 반환

def listSum(tempList):
    sum = 0
    for i in tempList:
        sum = sum + i
    return sum

if __name__ == "__main__":
    tempList = [i for i in range(1, 11)]
    print(tempList)

    sum = listSum(tempList)
    print(tempList, "->", sum)