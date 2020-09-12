# 2차원 리스트 행렬

list1, list2 = [], []

list1 = [i * 5 + j for i in range(5) for j in range(5)]
print(list1)

value = 1
for i in range(0, 5):
    for j in range(0, 5):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []
print(list2)

sum = 0;
for i in range(5):
    for j in range(5):
        print(f"[{list2[i][j]}]", end='')
        sum = sum + list2[i][j]
    print()
print("sum :", sum)