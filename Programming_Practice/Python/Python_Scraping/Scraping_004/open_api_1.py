import requests
import bs4

endpoint = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?"
serviceKey = "xqhT19uqLKmUuUxiUk6By%2FkUkZHlqQfalicqhc3oYnPy4KoA%2FK%2BM8EQVYGOaBBtfRMfqs6SQ1ei%2F8VPZgE6VlA%3D%3D"

numOfRows = "10"
pageSize = "1"
pageNo = "1"
MobileOS = "ETC"
MobileApp = "AppTest"
arrange = "A"
contentTypeId = "15"
areaCode = "3"
sigunguCode = "2"
listYN = "Y"

paramset = "serviceKey=" + serviceKey \
        + "&numOfRows=" + numOfRows \
        + "&pageSize=" + pageSize \
        + "&pageNo=" + pageNo \
        + "&MobileOS=" + MobileOS \
        + "&MobileApp=" + MobileApp \
        + "&arrange=" + arrange \
        + "&contentTypeId=" + contentTypeId \
        + "&areaCode=" + areaCode \
        + "&sigunguCode=" + sigunguCode \
        + "&listYN=" + listYN + "&_type=json"

url = endpoint + paramset
print(url)

result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
print(bs_obj)