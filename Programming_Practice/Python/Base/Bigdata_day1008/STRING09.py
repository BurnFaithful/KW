# 양쪽에 괄호가 없으면 괄호를 붙이고, 없으면 그대로 출력

s = input("문자를 입력 : ")

if s.startswith('(') and s.endswith(')'):
    print(s)
else:
    print(f"({s})")