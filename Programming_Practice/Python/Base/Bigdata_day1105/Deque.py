from collections import deque

if __name__ == "__main__":
    test_deque = deque()

    test_deque.append(1)
    test_deque.append(2)
    test_deque.appendleft(3)
    test_deque.appendleft(4)
    test_deque.appendleft(5)
    test_deque.appendleft(6)
    test_deque.append(7)
    test_deque.append(8)
    test_deque.append(9)
    test_deque.append(10)

    test_deque.pop()
    test_deque.popleft()

    print(test_deque)