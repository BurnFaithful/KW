import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

item_lis = bs_obj.select("ul.an_l > li.an_item > a > span.an_txt")

for i in item_lis:
    print(i.text)

item_at_item = bs_obj.findAll("li", {"class": "at_item"})
# for i in item_at_item:
#     print(i.text)