# 구구단 퀴즈 -> 5문제, 사용자 정답, 2초 내에 맞춰야 정답으로 인정
import time
import random

score = 0
while True:
    for i in range(5):
        question_dan = random.randint(2, 9)
        question_value = random.randint(1, 9)
        answer = question_dan * question_value

        start = time.perf_counter()

        user_answer = int(input(f"{question_dan} * {question_value} = "))

        end = time.perf_counter()
        elapsed_time = end - start

        if user_answer == answer and elapsed_time <= 2:
            print("정답입니다.")
            score += 1
        elif user_answer != answer:
            print("오답입니다.")
        elif elapsed_time > 2:
            print("시간 초과입니다.")

        print("당신의 점수는 {}점입니다.".format(score * 20))

    while True:
        restart = input("게임을 다시 하시겠습니까?(Y/N)")
        if restart is 'Y':
            continue
        elif restart is 'N':
            print("게임 종료")
            break
        else:
            print("잘못된 입력")

