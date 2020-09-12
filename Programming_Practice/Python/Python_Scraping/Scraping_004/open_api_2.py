from urllib.parse import quote
import requests
import bs4

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey = "xqhT19uqLKmUuUxiUk6By%2FkUkZHlqQfalicqhc3oYnPy4KoA%2FK%2BM8EQVYGOaBBtfRMfqs6SQ1ei%2F8VPZgE6VlA%3D%3D"

Q0 = quote("서울특별시") # 한글 인코딩 메서드
# Q1 = quote("강남구")
# QT = "1"
# QN = quote("삼성약국")
ORD = "NAME"
pageNo = "1"
startPage = "1"
numOfRows = "5000"
pageSize = "10"

paramset = "serviceKey=" + serviceKey \
        + "&numOfRows=" + numOfRows \
        + "&pageSize=" + pageSize \
        + "&pageNo=" + pageNo \
        + "&startPage=" + startPage \
        + "&Q0=" + Q0 \
        + "&ORD=" + ORD #\
        # + "&Q1=" + Q1 \
        # + "&QT=" + QT \
        # + "&QN=" + QN \
           # + "&_type=json"

url = endpoint + paramset
print(url)

result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
# print(bs_obj)
items = bs_obj.findAll("item")

count = 0
for item in items:
    tagged_item = item.find("dutytime1c")
    if tagged_item != None:
        close_time = int(tagged_item.text)
        if close_time > 2100:
            count += 1
            print(item.find("dutyname").text)
    # print(tagged_item)

# print("서울특별시 내 월요일 9시 이후까지 하는 약국의 수 : " + str(count))