# 문자열 함수 count, find, index

ss = "Process finished with exit code"

res = ss.count('i')
print(res)
res = ss.count('sh')
print(res)

res = ss.find('with')
print(res)
res = ss.find('P')
print(res)
res = ss.find('dfsf')
print(res)

res = ss.index('fi')
print(res)
# res = ss.index('dfsf')
# print(res)

res = ss.startswith('Pro')
print(res)
res = ss.startswith('ro')
print(res)

res = ss.endswith('code')
print(res)
res = ss.endswith('cod')
print(res)