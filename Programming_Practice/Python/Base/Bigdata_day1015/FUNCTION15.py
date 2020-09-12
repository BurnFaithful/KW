# 반환 여러개 (변수 여러개, 리스트)

def circleProc(radius, height):
    cirArea = radius * radius * 3.14159265
    cirVol = cirArea * height

    return cirArea, cirVol


if __name__ == "__main__":
    radius = float(input("반지름 입력 >> "))
    height = float(input("높이 입력 >> "))
    area, vol = circleProc(radius, height)

    print(f"반지름 {radius}인 원의 넓이 : {area}")
    print(f"반지름 {radius}, 높이 {height}인 원기둥의 부피 : {vol}")