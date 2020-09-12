# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
# import urllib.request
import requests
from urllib.parse import urlparse

keyword = "광운대학교"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + keyword # xml 결과

result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-id": "kdVtaStlHMFsOC2kiSsN",
                               "X-Naver-Client-Secret": "1_dkg4JCO0"})

# print(result.json())
json_obj = result.json()
print(json_obj['lastBuildDate'])
print(json_obj['total'])
print(json_obj['start'])
print(json_obj['display'])
# for item in json_obj['items']:
#     print(item)