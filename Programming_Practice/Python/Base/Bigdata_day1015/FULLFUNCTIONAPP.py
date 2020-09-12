# 1. 반복 기초 예제 -> Loopbasic
# 2. 구구단 한 단만 출력 -> OneGugudan
# 3. 콘솔 재입력 -> InputConsole
# 4. 전체 구구단 출력 -> FullGugudan
# 5. 별모양 출력 -> PrintStar
# 6. 삼각형 별모양 출력 -> PrintTriangle
# 7. 구구단 게임 -> GugudanGame
# 8. 종료
from Bigdata_day1015.funcmodule import *

# def Loopbasic():
#     i = 50
#
#     while i > 0:
#         print(i, end=' ')
#         i -= 1
#     print()
#
#     for j in range(50, -1, -1):
#         print(j, end=' ')
#
#
# def OneGugudan():
#     dan = int(input("몇 단을 출력할지 : "))
#     for i in range(1, 10):
#         print(f"{dan} * {i} = {dan * i}")
#
#
# def InputConsole():
#     import os
#
#     while True:
#         dan = input("몇 단을 출력할지 : ")
#         if dan.isalpha() or dan == '':
#             os.system('cls')
#         else:
#             break
#     dan = int(dan)
#     for i in range(1, 10):
#         print(f"{dan} * {i} = {dan * i}")
#
#
# def FullGugudan():
#     for i in range(2, 10):
#         print(f"======={i}단======")
#         for j in range(1, 10):
#             print(f"{i} * {j} = {i * j}")
#     print("-----------------------------------", end='')
#     for i in range(1, 10):
#         print()
#         for j in range(2, 10):
#             print(f"{j} * {i} = {i * j:>2}", end='  ')
#
#
# def PrintStar():
#     num = int(input("출력할 별 수 입력>> "))
#
#     for i in range(1, num + 1):
#         for j in range(i):
#             print("*", end='')
#         print()
#
#
# def PrintTriangle():
#     num = int(input("출력할 별 수 입력>> "))
#
#     for i in range(1, num + 1):
#         for j in range(num - i):
#             print(' ', end='')
#         for k in range(i * 2 - 1):
#             print("*", end='')
#         print()
#
#
# def GugudanGame():
#     # 구구단 퀴즈 -> 5문제, 사용자 정답, 2초 내에 맞춰야 정답으로 인정
#     import time
#     import random
#
#     score = 0
#     while True:
#         for i in range(5):
#             question_dan = random.randint(2, 9)
#             question_value = random.randint(1, 9)
#             answer = question_dan * question_value
#
#             start = time.perf_counter()
#
#             user_answer = int(input(f"{question_dan} * {question_value} = "))
#
#             end = time.perf_counter()
#             elapsed_time = end - start
#
#             if user_answer == answer and elapsed_time <= 2:
#                 print("정답입니다.")
#                 score += 1
#             elif user_answer != answer:
#                 print("오답입니다.")
#             elif elapsed_time > 2:
#                 print("시간 초과입니다.")
#
#             print("당신의 점수는 {}점입니다.".format(score * 20))
#
#         while True:
#             restart = input("게임을 다시 하시겠습니까?(Y/N)")
#             if restart is 'Y':
#                 continue
#             elif restart is 'N':
#                 print("게임 종료")
#                 break
#             else:
#                 print("잘못된 입력")
#
#
# def MenuDisplay():
#     print("1. 반복 기초 예제")
#     print("2. 구구단 한 단만 출력")
#     print("3. 콘솔 재입력")
#     print("4. 전체 구구단 출력")
#     print("5. 별모양 출력")
#     print("6. 삼각형 별모양 출력")
#     print("7. 구구단 게임")
#     print("8. 종료")
#
#
# def switch(command):
#     return {1: Loopbasic, 2: OneGugudan, 3: InputConsole,
#             4: FullGugudan, 5: PrintStar, 6: PrintTriangle,
#             7: GugudanGame, 8: lambda: print("종료")}.get(command, lambda: print("잘못된 입력"))


def run():
    MenuDisplay()
    while True:
        print()
        command = int(input("입력하세요(1 ~ 8) >>"))

        func = switch(command)
        func()
        if command == 8:
            break
        # if command >= 1 and command <= 8:
        #     if command == 1:
        #         Loopbasic()
        #     elif command == 2:
        #         OneGugudan()
        #     elif command == 3:
        #         InputConsole()
        #     elif command == 4:
        #         FullGugudan()
        #     elif command == 5:
        #         PrintStar()
        #     elif command == 6:
        #         PrintTriangle()
        #     elif command == 7:
        #         GugudanGame()
        #     elif command == 8:
        #         print("종료.")
        #         break
        # else:
        #     print("잘못된 입력")


if __name__ == "__main__":
    run()