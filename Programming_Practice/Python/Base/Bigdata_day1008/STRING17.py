# 주민번호 앞자리 6자리 입력

import datetime

num = input("주민번호 앞자리 입력: ")
year = '19' + num[:2]
month = num[2:4]
day = num[4:6]
print(f"당신은 {year} 년에 태어났군요.")
print(f"당신의 생일은 {month}월 {day}일 이군요.")
age = datetime.date.today().year - int(year)
print(f"당신은 올해 {age} 살이군요.")