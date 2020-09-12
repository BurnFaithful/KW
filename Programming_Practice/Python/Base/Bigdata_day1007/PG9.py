# 15분 이내는 무료
# 15분 단위로 1000원씩 추가

print("=== 주차료 계산 프로그램 ===")
parkingtime = int(input("주차시간 입력 : "))
print(f"주차시간 : {parkingtime}")
parkingcost = (parkingtime // 15) * 1000
print(f"주차요금 : {parkingcost}")