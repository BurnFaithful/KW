# 리스트 : 1, 2, 3, 4, 5, 6, 7, 8, 9
# i의 자노드 : 왼쪽 i * 2, 오른쪽 i * 2 + 1
# i의 부노드 : i // 2


class BinaryHeap:
    def __init__(self, item):
        self.item = item # item[0]는 사용하지 않음.
        self.N = len(item) - 1

    def createHeap(self):
        for i in range(self.N // 2, 0, -1):
            self.downHeap(i)

    def insert(self, key):
        self.N += 1
        self.item.append(key)
        self.upHeap(self.N)

    def delete_min(self):
        if self.N == 0:
            print("힙이 비었습니다.")
            return None

        min = self.item[1]
        self.item[1], self.item[-1] = self.item[-1], self.item[1]
        del self.item[-1]
        self.N -= 1
        self.downHeap(1)
        return min

    def downHeap(self, i):
        while 2 * i < self.N:
            k = 2 * i
            if k < self.N and self.item[k][0] > self.item[k + 1][0]: #item[k][0] : 키, item[k][1] 데이터
                k += 1

            if self.item[i][0] < self.item[k][0]:
                break

            self.item[i], self.item[k] = self.item[k], self.item[i]
            i = k

    def upHeap(self, i):
        while i > 1 and self.item[i // 2][0] > self.item[i][0]:
            self.item[i // 2], self.item[i] = self.item[i], self.item[i // 2]
            i = i // 2

    def printHeap(self):
        print("MinHeap=", end='')
        for i in range(1, self.N + 1):
            print(f"[{self.item[i][0]}:{self.item[i][1]}]", end='')
        print()
        print(f"Heap Size={self.N}")