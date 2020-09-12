# 구구단 전체

for i in range(2, 10):
    print(f"======={i}단======")
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
print("-----------------------------------", end='')
for i in range(1, 10):
    print()
    for j in range(2, 10):
        print(f"{j} * {i} = {i * j:>2}", end='  ')