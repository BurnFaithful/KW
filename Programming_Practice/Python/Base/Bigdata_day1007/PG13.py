# BMI = 몸무게 / 키 * 키

height = int(input("키가 몇 cm입니까? "))
weight = int(input("몸무게가 몇 kg입니까? "))
height = height / 100
bmi = weight / (height * height)

if bmi <= 18.5:
    print(f"당신의 BMI는 {bmi:.2f}로 저체중입니다.")
elif bmi > 18.5 and bmi <= 22.9:
    print(f"당신의 BMI는 {bmi:.2f}로 정상입니다.")
elif bmi >= 23.0 and bmi <= 24.9:
    print(f"당신의 BMI는 {bmi:.2f}로 과체중입니다.")
elif bmi >= 25.0 and bmi <= 29.9:
    print(f"당신의 BMI는 {bmi:.2f}로 비만입니다.")
elif bmi >= 30.0:
    print(f"당신의 BMI는 {bmi:.2f}로 고도비만입니다.")