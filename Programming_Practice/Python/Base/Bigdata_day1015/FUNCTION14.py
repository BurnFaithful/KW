# 원의 넓이 : 반지름 * 반지름 * PI
# 원의 둘레 : 2 * PI * 반지름

def circleArea(radius):
    area = radius * radius * 3.14
    return area

def circleVolume(radius):
    volume = 2 * 3.14 * radius
    return volume

if __name__ == "__main__":
    radius = int(input("반지름 입력 >> "))
    print(f"반지름 {radius}인 원의 넓이 : {circleArea(radius)}")
    print(f"반지름 {radius}인 원의 둘레 : {circleVolume(radius)}")