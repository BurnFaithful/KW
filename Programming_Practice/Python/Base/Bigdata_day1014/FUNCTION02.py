def FindMax(a, b, c):
    bigNumber = 0
    if a > b: bigNumber = a
    else: bigNumber = b

    if bigNumber < c: bigNumber = c

    return bigNumber


if __name__ == "__main__":
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    c = int(input("Enter Third Number : "))

    print(f"가장 큰 수 : {FindMax(a, b, c)}")