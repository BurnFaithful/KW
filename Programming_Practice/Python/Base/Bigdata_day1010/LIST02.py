# 리스트 사용법
aa = list()
for i in range(4):
    aa.append(0)
sum_value = 0

# for index, i in enumerate(aa):
#     aa[index] = int(input(str(index + 1) + '번째 숫자: '))
# print(aa)

aa = [int(input(str(index + 1) + '번째 숫자: ')) for index, i in enumerate(aa)]
print(aa)

sum_value = sum(aa)
print('총합:', sum_value)