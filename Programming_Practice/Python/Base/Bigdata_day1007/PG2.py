# 1씩 더하여 암호화
a = input("원문 >> ")
encode = ""
for i in a:
    i = ord(i) + 1
    i = chr(i)
    encode += i

print("암호 >>", encode)

decode = ""
# 1씩 빼서 복호화
for i in encode:
    i = chr(ord(i) - 1)
    decode += i

print("복호 >>", decode)