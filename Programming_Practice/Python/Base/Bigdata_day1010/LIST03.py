aa = list()
bb = list()
value = 0

for _ in range(100):
    aa.append(value)
    value += 2
print(aa)

# for i in range(100):
#     bb.append(aa[99 - i])
bb = aa[::-1]
print(bb)