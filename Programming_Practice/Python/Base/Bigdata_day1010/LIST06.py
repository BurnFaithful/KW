aa = [10, 20, 30]
aa[1] = 200
print(aa)

bb = [10, 20, 30]
bb[1:2] = [200, 201]
print(bb)

cc = [10, 20, 30]
cc[1] = [200, 201]
print(cc)

dd = [10, 20, 30]
del(dd[1])
print(dd)