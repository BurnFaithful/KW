# 웹 브라우저 모듈

import webbrowser # PC Default 브라우저 이용

# url = "http://www.google.com"

# webbrowser.open(url, 1)

a = []
print("번역할 문장을 입력하세요")
while True:
    text = input("-> ")
    if text == '끝':
        a = "\n".join(a)
        break
    else:
        a.append(text)

print(a)

url = "https://translate.google.co.kr/#ko/en/" + a
webbrowser.open(url, 1)