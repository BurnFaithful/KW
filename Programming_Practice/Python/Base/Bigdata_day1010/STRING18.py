# 주민번호 전부 입력

import datetime

num = input("주민번호 13자리 입력: ")
year = ""
sex = int(num[7])
if sex == 1 or sex == 2:
    year = '19' + num[:2]
elif sex == 3 or sex == 4:
    year = '20' + num[:2]
month = num[2:4]
day = num[4:6]
print(f"당신은 {year} 년에 태어났군요.")
print(f"당신의 생일은 {month}월 {day}일 이군요.")
age = datetime.date.today().year - int(year)
print(f"당신은 올해 {age} 살이군요.")
if sex == 1 or sex == 3: print("당신은 남성이군요.")
elif sex == 2 or sex == 4: print("당신은 여성이군요")