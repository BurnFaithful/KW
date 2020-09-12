# 윤년
# 4로 나누어 떨어지면 윤년
# 그 중 100으로 나누어 떨어지면 윤년이 아님
# 400으로 나누어 떨어지는 년도는 무조건 윤년
import calendar

year = int(input("년도 : "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}년은 윤년입니다.")
    calendar.prmonth(year, 2)
else:
    print(f"{year}년은 윤년이 아닙니다.")
    calendar.prmonth(year, 2)