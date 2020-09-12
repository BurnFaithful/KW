# 문자열 분리 및 결합
# split, splitlines, join

ss = "하나 둘 셋"
res = ss.split()
print(ss)
print(res)

ss = "하나:둘:셋"
res = ss.split(':')
print(res)

ss = "하나\n둘\n셋"
res = ss.splitlines()
print(ss)
print(res)

ss = '%'
res = ss.join('파이썬')
print(res)