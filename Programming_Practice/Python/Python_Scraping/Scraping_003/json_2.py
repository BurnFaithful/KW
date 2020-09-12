from urllib.request import urlopen
import json

# from_date = "2019-01-01"
# to_date = "2019-12-23"
# url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/" \
#         + from_date + "/edate/" + to_date
# text = urlopen(url)
# json_objs = json.load(text)

# print(json_objs)

url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/1972-01-01/edate/2019-12-23"
text = urlopen(url)
json_objs = json.load(text)

for item in json_objs:
    print(item['date'] + "@" + item['settlement'])
    # print(item['settlement'])

