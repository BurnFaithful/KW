# IF 4가지 형식
# 단독
# if else
# if elif else
# if 중첩

num = int(input("정수 입력 : "))

if num > 100:
    print("100보다 크다")

if num > 100:
    print("100보다 크다")
else:
    print("100보다 작다")

if num > 100:
    print("100보다 크다")
elif num >= 90 and num < 100:
    print("90보다 크거나 같고 100보다 작다")

# A와 B가 같고, B와 C가 같으면 A와 C는 같다
a = 10; b = 10; c = 20
if a == b:
    if b == c:
        if a == c:
            print("A와 C는 같다")
    else:
        print("A와 C는 같지 않다")
else:
    print("A와 C는 같지 않다")