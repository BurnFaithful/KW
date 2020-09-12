PI = 3.14159265


def radiusIn():
    return float(input("반지름 입력 : "))


def processCircle(radius, PI):
    return PI * radius * radius


def printCircle(radius, area):
    print(f"반지름이 {radius:.2f}인 원의 넓이 : {area:.2f}")


# # 입력부 => RadiusIn() 매개변수 x, float 반환값 1개
# r = float(input("반지름 입력 : "))
#
# # 처리부 => ProcessCircle() 매개변수 2개, float 반환값 1개
# circleArea = PI * r * r
#
# # 출력부 => PrintCircle() 매개변수 2개
# print(f"반지름이 {r:.2f}인 원의 넓이 : {circleArea:.2f}")

if __name__ == "__main__":
    r = radiusIn()
    printCircle(r, processCircle(r, PI))
