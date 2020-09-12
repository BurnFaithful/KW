from Bigdata_day1111.BST import *

def menu():
    print("==========Menu==========")
    print("1. insert node / 2. delete min / 3. delete max / 4. delete item / 5. ascending print / 0. exit")
    print("==========Menu==========")


if __name__ == "__main__":
    bst = BinarySearchTree(BSTNode(90, '수박'))
    bst.put(80, '배')
    bst.put(70, '멜론')
    bst.put(50, '라임')
    bst.put(60, '망고')
    bst.put(20, '체리')
    bst.put(30, '포도')
    bst.put(35, '오렌지')
    bst.put(10, '귤')
    bst.put(15, '바나나')
    bst.put(45, '레몬')
    bst.put(40, '키위')
    print("테스트 값들을 초기화했습니다.")

    while True:
        menu()
        command = int(input("command input >> "))
        if command == 1:
            key = int(input("insert key input >> "))
            value = input("insert value input >> ")
            bst.put(key, value)
            print(f"[{key} : {value}]를 추가했습니다.")
        elif command == 2:
            bst_min = bst.min(bst.root)
            bst.delete_min()
            print(f"최소값 [{bst_min.key} : {bst_min.value}]를 삭제했습니다.")
        elif command == 3:
            bst_max = bst.max(bst.root)
            deleteMax = bst.delete_max()
            print(f"최대값 [{bst_max.key} : {bst_max.value}]를 삭제했습니다.")
        elif command == 4:
            key = int(input("delete key input >> "))
            bst_deleteNode = bst.get(key)
            bst.delete(key)
            print(f"해당 키와 맞는 노드 [{bst_deleteNode.key} : {bst_deleteNode.value}]를 삭제했습니다.")
        elif command == 5:
            bst.inOrder(bst.root)
            print()
        elif command == 0:
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력")


