import urllib.request
import bs4

url = "https://news.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

it_news = bs_obj.select("#section_it ul.mlist2 > li > a > strong")

for i in it_news:
    print(i.text)
# print(it_news)