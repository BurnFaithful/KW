# 리스트 조작 함수 그 외

mylist = [30, 10, 20]
print("현재 리스트 :", mylist)

mylist.append(40)
print("append(40) 후 :", mylist)

res = mylist.pop()
print("pop()으로 추출한 값 :", res)
print("현재 리스트 :", mylist)

mylist.sort()
print("sort() 후 :", mylist)

mylist.reverse()
print("reverse() 후 :", mylist)

val = mylist.index(20)
print("index(20) :", val)

mylist.insert(2, 222)
print("insert(2, 222) 후 :", mylist)

mylist.remove(222)
print("remove(222) 후 :", mylist)

mylist.extend([77, 88, 99])
print("extend([77, 88, 99]) 후 :", mylist)

cnt = mylist.count(77)
print("현재 리스트의 77 개수 :", cnt)

ary = [1, 3, 5, 6, 7, 4, 10, 66, 9, 99]
temp = sorted(ary)
print(ary)
print(temp)