import os
from CustomClass_YM import ConsoleUtil
from Bigdata_day1030.EmptyException import EmptyError
from Bigdata_day1030.Node import DLNode


class DLinkedList:
    def __init__(self):
        self.headNode = None
        self.tailNode = None
        self.size = 0

    def __str__(self):
        linkedList = list()
        iterNode = self.headNode
        if iterNode is None:
            return "List is Empty."

        while iterNode.next is not None:
            linkedList.append(iterNode.value)
            iterNode = iterNode.next
        linkedList.append(iterNode.value)
        return ' <-> '.join(map(str, linkedList))


    def size(self):
        return self.size


    def isEmpty(self):
        return self.size == 0


    def pushFrontNode(self, value):
        if self.isEmpty():
            self.headNode = DLNode(value, None, None)
            self.tailNode = self.headNode
        else:
            nextNode = self.headNode
            self.headNode = DLNode(value, None, self.headNode)
            nextNode.prev = self.headNode

        self.size += 1


    def pushBackNode(self, value):
        if self.isEmpty():
            self.pushFrontNode(value)
            return
        else:
            prevNode = self.tailNode
            self.tailNode = DLNode(value, self.tailNode, None)
            prevNode.next = self.tailNode

        self.size += 1


    def insertNode(self, value, index):
        if self.size <= index - 1:
            raise IndexError("Out of index.")

        if index == 0:
            self.pushFrontNode(value)
        elif index == self.size:
            self.pushBackNode(value)

        elif index >= self.size // 2: # 인덱스가 사이즈의 절반 이상이면 tail에서부터 탐색
            iterNode = self.tailNode
            for _ in range(self.size - index):
                iterNode = iterNode.prev
            pushNode = DLNode(value, iterNode, iterNode.next)
            iterNode.next = pushNode
            iterNode.next.prev = pushNode
        elif index < self.size // 2: # 인덱스가 사이즈의 절반에 못 미치면 head에서부터 탐색
            iterNode = self.headNode
            for _ in range(index):
                iterNode = iterNode.next
            pushNode = DLNode(value, iterNode.prev, iterNode)
            iterNode.prev.next = pushNode
            iterNode.prev = pushNode

        self.size += 1


    def removeFrontNode(self):
        if self.isEmpty():
            raise EmptyError("Underflow")

        if self.size == 1:
            self.headNode = None
            self.tailNode = None
        else:
            self.headNode = self.headNode.next
            self.headNode.prev = None

        self.size -= 1


    def removeBackNode(self):
        if self.isEmpty():
            raise EmptyError("Underflow")

        if self.size == 1:
            self.headNode = None
            self.tailNode = None
        else:
            self.tailNode = self.tailNode.prev
            self.tailNode.next = None

        self.size -= 1


    def removeIndexNode(self, index):
        if self.size < index - 1:
            raise IndexError("Out of index.")

        self.size -= 1


    def modifyNodeValue(self, value, index):
        self.getNode(index).value = value
        print(f"{self.getNode(index).value} => {value}")


    def findNode(self, value):
        iterNode = self.headNode
        for i in range(self.size):
            if iterNode.value == value:
                return i
            iterNode = iterNode.next
        return None


    def getNode(self, index):
        if self.size <= index:
            print("리스트의 범위를 벗어났습니다.")
            # raise IndexError("Out of index.")
            return None
        elif index < 0:
            print("잘못된 인덱스 입력입니다.")
            # raise IndexError("invalidate index.")
            return None

        if index >= self.size // 2:
            iterNode = self.tailNode
            for _ in range(self.size - index - 1):
                iterNode = iterNode.prev
            return iterNode.value
        else:
            iterNode = self.headNode
            for _ in range(index):
                iterNode = iterNode.next
            return iterNode.value


    def printAll(self):
        print(self)


def menu():
    print("======더블 링크드 리스트======")
    print("1. 앞에 노드 삽입 / 2. 뒤에 노드 삽입 / 3. 특정 인덱스에 노드 삽입 / 4. 앞의 노드 삭제 / 5. 뒤의 노드 삭제 / 6. 노드 검색(값) \
/ 7. 노드 검색(인덱스) / 8. 리스트 출력 / 9. 종료")


if __name__ == "__main__":
    dll = DLinkedList()

    while True:
        menu()
        command = ConsoleUtil.inputFilter(1, 9, menu)

        if command == 1:
            value = input("넣을 값 >> ")
            dll.pushFrontNode(value)
        elif command == 2:
            value = input("넣을 값 >> ")
            dll.pushBackNode(value)
        elif command == 3:
            index = int(input("넣을 인덱스 >> "))
            value = input("넣을 값 >> ")
            dll.insertNode(value, index)
        elif command == 4:
            dll.removeFrontNode()
        elif command == 5:
            dll.removeBackNode()
        elif command == 6:
            value = input("검색할 값 >> ")
            print(f"{dll.findNode(value)} 번째 인덱스에 있음.")
        elif command == 7:
            value = int(input("검색할 인덱스 >> "))
            print(f"{value}번째 인덱스의 값은 {dll.getNode(value)}입니다.")
        elif command == 8:
            dll.printAll()
        elif command == 9:
            print("Program Exit")
            os._exit(0)