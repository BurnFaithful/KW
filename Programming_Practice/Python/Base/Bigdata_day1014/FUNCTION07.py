def inputValue():
    x = int(input("작은 수 : "))
    y = int(input("큰 수 : "))
    return x, y

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
        else:
            print(i, end=' ')
            return 1

def checkPrimeProcess(start, end):
    count = 0
    for i in range(start, end + 1):
        # for j in range(2, i):
        #     if i % j == 0:
        #         break
        # else:
        #     print(i, end=' ')
        #     count += 1
        count += isPrime(i)
    else:
        print()

    return count

if __name__ == "__main__":
    x, y = inputValue()
    count = checkPrimeProcess(x, y)
    print(f"소수는 모두 {count}개 입니다.")