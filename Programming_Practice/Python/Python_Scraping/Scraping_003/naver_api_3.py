import requests
from urllib.parse import urlparse


# display_count = 100
# keyword = "광운대학교"
def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
          + "&display=" + str(display) \
          + "&start=" + str(start) # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + keyword # xml 결과

    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-id": "kdVtaStlHMFsOC2kiSsN",
                                   "X-Naver-Client-Secret": "1_dkg4JCO0"})
    return result.json()


def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100, page)
    for item in json_obj['items']:
        title = item['title'].replace('<b>', '').replace('</b>', '')
        print(title + "@" + item['bloggername'] + "@" + item['link'])

# print(result.json())
# json_obj = result.json()
# print(get_api_result("광운대학교", 100, 101))
# for item in json_obj['items']:
#     print(item)
# for item in json_obj['items']:
#     print(item['title'].replace('<b>', '').replace('</b>', ''))
#     print(item['link'])
# print("display :", str(json_obj['display']))
# print("start :", str(json_obj['start']))
# print('items :', str(len(json_obj['items'])))


keyword = "광운대학교"
for i in range(5):
    call_and_print(keyword, i * 100 + 1)