# 문자열 채우기

ss = "파이썬"
print(ss.center(11))
print(ss.center(11, '-'))
print(ss.ljust(11))
print(ss.rjust(11))
print(ss.zfill(11))

# 문자열 형식, 형태, 구성
s1 = "1234"
print(s1.isdigit())
s1 = "abcd"
print(s1.isalpha())
s1 = "1"
print(s1.isnumeric())
s1 = "abcdef123"
print(s1.isalnum())
s1 = " "
print(s1.isspace())