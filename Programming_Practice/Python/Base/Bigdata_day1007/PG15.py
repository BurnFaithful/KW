# 1부터 50까지의 소수를 모두 출력하기

def prime_check(n):
    for i in range(2, n):
        if n % i == 0: return False
    return True

prime = []
for i in range(2, 51):
    if prime_check(i) is True: prime.append(i)

print(prime)