# 2019/10/08 -> 2019년10월08일

ss = input("날짜: 년/월/일 입력 >> ")

sslist = ss.split('/')
print(sslist)

print("입력하신 날짜의 10년 후 -> ", end='')
print(f"{int(sslist[0]) + 10}년{sslist[1]}월{sslist[2]}일")