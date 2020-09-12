import os
from CustomClass_YM import ConsoleUtil
from Bigdata_day1030.EmptyException import EmptyError
from Bigdata_day1030.Node import SLNode


class CLinkedList:
    def __init__(self):
        self.headNode = None
        self.tailNode = None
        self.size = 0

    def __str__(self):
        linkedList = list()
        iterNode = self.headNode
        if iterNode is None:
            return "List is Empty."

        for _ in range(self.size):
            linkedList.append(iterNode.value)
            iterNode = iterNode.link
        linkedList.append(iterNode.value)
        return ' -> '.join(map(str, linkedList))


    def size(self):
        return self.size


    def isEmpty(self):
        return self.size == 0


    def pushFrontNode(self, value):
        if self.isEmpty():
            pushNode = SLNode(value, self.headNode)
            self.headNode = pushNode
            self.headNode.link = pushNode
            self.tailNode = self.headNode
        else:
            self.headNode = SLNode(value, self.headNode)
            self.tailNode.link = self.headNode

        self.size += 1


    def pushBackNode(self, value):
        if self.isEmpty():
            self.pushFrontNode(value)
            return
        else:
            pushNode = SLNode(value, self.headNode)
            self.tailNode.link = pushNode
            self.tailNode = pushNode

        self.size += 1


    def insertNode(self, value, index):
        if self.size <= index - 1:
            raise IndexError("Out of index.")

        if index == 0:
            self.pushFrontNode(value)
        elif index == self.size:
            self.pushBackNode(value)
        else:
            iterNode = self.headNode
            for _ in range(index - 1):
                iterNode = iterNode.link
            iterNode.link = SLNode(value, iterNode.link.link)

        self.size += 1


    def removeFrontNode(self):
        if self.isEmpty():
            raise EmptyError("Underflow")

        if self.size == 1:
            self.headNode = None
            self.tailNode = None
        else:
            self.headNode = self.headNode.link
            self.tailNode.link = self.headNode

        self.size -= 1


    def removeBackNode(self):
        if self.isEmpty():
            raise EmptyError("Underflow")

        if self.size == 1:
            self.headNode = None
            self.tailNode = None
        else:
            iterNode = self.headNode
            for _ in range(self.size - 2):
                iterNode = iterNode.link
            self.tailNode = iterNode
            self.tailNode.link = self.headNode

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
            iterNode = iterNode.link
        return None


    def getNode(self, index):
        if self.size <= index:
            raise IndexError("Out of index.")

        iterNode = self.headNode
        for _ in range(index):
            iterNode = iterNode.link
            return iterNode.value
        return None


    def printAll(self):
        print(self)


def menu():
    print("======환형 링크드 리스트======")
    print("1. 앞에 노드 삽입 / 2. 뒤에 노드 삽입 / 3. 특정 인덱스에 노드 삽입 / 4. 앞의 노드 삭제 / 5. 뒤의 노드 삭제 / 6. 노드 검색(값) \
/ 7. 노드 검색(인덱스) / 8. 리스트 출력 / 9. 종료")


if __name__ == "__main__":
    cll = CLinkedList()

    while True:
        menu()
        command = ConsoleUtil.inputFilter(1, 9, menu)

        if command == 1:
            value = input("넣을 값 >> ")
            cll.pushFrontNode(value)
        elif command == 2:
            value = input("넣을 값 >> ")
            cll.pushBackNode(value)
        elif command == 3:
            index = int(input("넣을 인덱스 >> "))
            value = input("넣을 값 >> ")
            cll.insertNode(value, index)
        elif command == 4:
            cll.removeFrontNode()
        elif command == 5:
            cll.removeBackNode()
        elif command == 6:
            value = input("검색할 값 >> ")
            cll.findNode(value)
        elif command == 7:
            value = int(input("검색할 인덱스 >> "))
            cll.getNode(value)
        elif command == 8:
            cll.printAll()
        elif command == 9:
            print("Program Exit")
            os._exit(0)