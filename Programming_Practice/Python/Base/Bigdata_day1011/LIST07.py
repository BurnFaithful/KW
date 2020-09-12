# 리스트 중복되는 값이 안 들어감

listID = list()
listID.append(2001)
listID.append(2002)
listID.append(2003)
listID.append(2003)

for i in listID:
    print(i, end=' ')

for m in listID:
    if listID.index(m) == 2:
        # print(f"{listID.index(m)} {m}")
        listID[2] = 'DDD'
print(listID)

