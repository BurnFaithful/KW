# 소수 판별
import math
import time

def decorator(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter() - start
        print(f"소요 시간 : {end} ms")

@decorator
def prime_for(num):
    for i in range(2, n):
        if i % num == 0:
            print(f"{num}은 소수입니다.")
        else:
            print(f"{num}은 소수가 아닙니다.")

@decorator
def prime_while_sqrt(num):
    success = True
    t = 2
    while t < math.sqrt(n):
        if n % t == 0:
            success = False
            break
        t += 1

n = int(input("어떤 수를 판별할까요? "))