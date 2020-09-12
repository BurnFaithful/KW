import os
from Bigdata_day1030.EmptyException import EmptyError
from Bigdata_day1030.LinkedList import SLNode
from CustomClass_YM import ConsoleUtil

class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__size = 0

    def __str__(self):
        pass

    @property
    def size(self):
        return self.__size

    @property
    def front(self):
        return self.__front

    @property
    def rear(self):
        return self.__rear

    def isEmpty(self):
        if self.__size == 0:
            return True
        return False

    def printAll(self):
        print(self)


    def enqueue(self, value):
        if self.isEmpty():
            self.__front = self.__rear = SLNode(value, None)
        else:
            self.__rear.link = SLNode(value, None)
            self.__rear = self.__rear.link

        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            print("큐가 비었습니다.")
            return

        if self.size == 1:
            self.__front = self.__rear = None
            self.__size -= 1
        else:
            dequeueNode = self.__front
            self.__front = dequeueNode.link
            self.__size -= 1
            return dequeueNode.value


    def peek(self):
        if self.isEmpty():
            print("큐가 비었습니다.")
            return

        return self.__front


def menu():
    print("=============== 큐 ===============")
    print("1. Enqueue / 2. Dequeue / 3. 픽(Peek) / 4. 사이즈(Size) / 5. 프론트(front) / 6. 레어(rear) / 7. 출력 / 8. 종료")


if __name__ == "__main__":
    queue = Queue()

    while True:
        menu()
        command = ConsoleUtil.inputFilter(1, 7, menu)

        if command == 1:
            value = input("넣을 값 >> ")
            queue.enqueue(value)
        elif command == 2:
            print(f"Dequeue된 노드의 값은 {queue.dequeue().value}입니다.")
        elif command == 3:
            print(f"Peek된 노드의 값은 {queue.peek().value}입니다.")
        elif command == 4:
            print(f"큐의 크기는 {queue.size}입니다.")
        elif command == 5:
            print(f"큐의 프론트는 {queue.front.value}입니다.")
        elif command == 6:
            print(f"큐의 레어는 {queue.rear.value}입니다.")
        elif command == 7:
            queue.printAll()
        elif command == 8:
            print("Program Exit")
            os._exit(0)