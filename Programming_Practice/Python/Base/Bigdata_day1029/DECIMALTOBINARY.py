# 10진수 -> 2진수 재귀적 호출

def decimal_to_binary(n):
    if n <= 1:
        print(n, end='')
    else:
        decimal_to_binary(n // 2)
        print(n % 2, end='')

if __name__ == "__main__":
    number = int(input("2진수로 바꿀 10진수 입력 >> "))
    decimal_to_binary(number)