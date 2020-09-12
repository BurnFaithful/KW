# fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, ...


def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibo_for(n):
    first, second = 0, 1
    if n == 1: return first
    elif n == 2: return second

    result = 0
    for _ in range(n - 2):
        result = first + second
        first = second
        second = result
    return result

def fibo_print_list(n):
    fiboList = list()
    first, second = 0, 1

    fiboList.append(first)
    fiboList.append(second)
    if n > 2:
        for i in range(n - 2):
            fiboList.append(fiboList[i - 2] + fiboList[i - 1])

    print(f"fiboList : {', '.join(map(str, fiboList))}")

if __name__ == "__main__":
    term = int(input("몇 번째 항? >> "))
    print(f"fibo({term}) : {fibo(term)}")
    print(f"fibo_for({term}) : {fibo_for(term)}")
    fibo_print_list(term)