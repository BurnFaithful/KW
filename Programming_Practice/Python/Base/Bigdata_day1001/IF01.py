kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
total = kor + eng + math
avg = total / 3

if avg < 0 or avg > 100:
    print("THE END")
else:
    if avg <= 100 and avg >= 90:
        print(f"총점:{total} 평균:{avg}, A+ Grade")
    elif avg <= 89 and avg >= 80:
        print(f"총점:{total} 평균:{avg}, B+ Grade")
    else:
        print(f"총점:{total} 평균:{avg}, C~F Grade")