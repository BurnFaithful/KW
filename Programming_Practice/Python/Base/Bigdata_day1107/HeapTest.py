from Bigdata_day1107.Heap import *

def menu():
    print("==========Menu==========")
    print("1. insert node / 2. delete heap / 3. print heap / 0. exit")
    print("==========Menu==========")


if __name__ == "__main__":
    a = [None]
    a.append([90, '수박'])
    a.append([80, '배'])
    a.append([70, '멜론'])
    a.append([50, '라임'])
    a.append([60, '망고'])
    a.append([20, '체리'])
    a.append([30, '포도'])
    a.append([35, '오렌지'])
    a.append([10, '귤'])
    a.append([15, '바나나'])
    a.append([45, '레몬'])
    a.append([40, '키위'])
    minHeap = BinaryHeap(a)
    # print("힙 구성 전의 트리 확인 : ", end='')
    # minHeap.printHeap()
    # minHeap.createHeap()

    # Test
    # print("최소 힙 확인 : ", end='')
    # minHeap.printHeap()
    # print("최소값[root] 삭제")
    # print(f"삭제된 루트 : {minHeap.delete_min()}")
    # minHeap.printHeap()
    # minHeap.insert([8, '사과'])
    # minHeap.printHeap()

    while True:
        menu()
        command = int(input("select menu >> "))

        if command == 1:
            key = int(input("key >> "))
            value = input("value >> ")
            minHeap.insert([key, value])
        elif command == 2:
            print(f"{minHeap.delete_min()} 삭제")
        elif command == 3:
            minHeap.printHeap()
        elif command == 0:
            print("종료합니다.")
            break
        else:
            print("잘못된 입력")