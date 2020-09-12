s = input("문자를 입력: ")

if s.isupper():
    s = s.lower()
elif s.islower():
    s = s.upper()
elif s.istitle():
    s = s.lower()

print(s)