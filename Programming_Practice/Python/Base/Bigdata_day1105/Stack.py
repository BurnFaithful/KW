import os
from Bigdata_day1030.EmptyException import EmptyError
from Bigdata_day1030.Node import SLNode
from CustomClass_YM import ConsoleUtil

class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def __str__(self):
        if self.isEmpty():
            return "Stack is Empty."

        items = list()
        iter = self.__top
        while iter.link is not None:
            items.append(iter.value)
            iter = iter.link
        items.append(iter.value)
        return '\n'.join(map(str, items))


    def printAll(self):
        print(self)

    @property
    def size(self):
        return self.__size

    @property
    def top(self):
        if self.isEmpty():
            print("스택이 비었습니다.")
            return
            # raise EmptyError("Stack is Empty.")

        return self.__top

    def isEmpty(self):
        if self.__size == 0:
            return True
        return False

    def push(self, value):
        self.__top = SLNode(value, self.__top)
        self.__size += 1

    def pop(self):
        if self.isEmpty():
            print("스택이 비었습니다.")
            return
            # raise EmptyError("Stack is Empty.")

        popNode = self.__top
        self.__top = self.__top.link
        self.__size -= 1
        return popNode

    def peek(self):
        if self.isEmpty():
            print("스택이 비었습니다.")
            return
            # raise EmptyError("Stack is Empty.")
        return self.__top


def menu():
    print("=============== 스택 ===============")
    print("1. 푸시(Push) / 2. 팝(Pop) / 3. 픽(Peek) / 4. 사이즈(Size) / 5. 탑 포인터(Top) / 6. 출력 / 7. 종료")


if __name__ == "__main__":
    stack = Stack()

    while True:
        menu()
        command = ConsoleUtil.inputFilter(1, 7, menu)

        if command == 1:
            value = input("넣을 값 >> ")
            stack.push(value)
        elif command == 2:
            print(f"Pop된 노드의 값은 {stack.pop().value}입니다.")
        elif command == 3:
            print(f"Peek된 노드의 값은 {stack.peek().value}입니다.")
        elif command == 4:
            print(f"스택의 크기는 {stack.size}입니다.")
        elif command == 5:
            print(f"스택의 탑 포인터는 {stack.top.value}입니다.")
        elif command == 6:
            stack.printAll()
        elif command == 7:
            print("Program Exit")
            os._exit(0)