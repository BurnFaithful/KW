# factorial


def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


def fac_for(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(f"fac(5) : {fac(5)}")
    print(f"fac_for(5) : {fac_for(5)}")