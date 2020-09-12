# Sort

b = [[0, 1, 8], [7, 9, 3], [9, 10, 1], [2, 3, 5]]
b.sort()
print(b)
b.sort(key=lambda x: x[2])
print(b)

# 수행시간 체크
import time
import random

startTime = time.perf_counter()

# for i in range(1000000):
#     print(i)
a = list()
for i in range(1000):
    for j in range(10000):
        b = list()
        b.append(random.randint(1, 1000))
    a.append(b)

endTime = time.perf_counter() - startTime

print(f"실행 시간 : {endTime:.4} sec")