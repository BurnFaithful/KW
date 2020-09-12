# break, continue
# 1 ~ 100까지 출력

for i in range(1, 101):
    if i == 20: break
    print(i, end=' ')

print()
for i in range(1, 101):
    if i == 20: continue
    print(i, end=' ')