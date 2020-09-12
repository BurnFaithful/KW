# 적정 몸무게 = (키 - 100) * 0.9
# 과체중 위험 기준 = 적정몸무게 * 1.2
# 저체중 위험 기준 = 적정몸무게 * 0.8

height = float(input("키가 몇 cm에요? "))
print(f"당신의 신장: {height:1}")
weight = (height - 100) * 0.9
print(f"적정 몸무게: {weight:1}")
print(f"과체중 위험 기준: {weight * 1.2}")
print(f"저체중 위험 기준: {weight * 0.8}")