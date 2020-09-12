import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0"}
main_url = 'http://jolse.com'
url = 'http://jolse.com/category/toners-mists/1019/'

result = requests.get(url, headers=headers)

bs_obj = BeautifulSoup(result.content, "html.parser")


def get_product_info(_url):
    result = requests.get(_url, headers=headers)
    prd_list = bs_obj.find("ul", {"class": "prdList"})
    prd_name = bs_obj.findAll("p", {"class:", "name"})
    prd_name = [i.find("span").text for i in prd_name]

    prd_cost = prd_list.findAll("ul")
    prd_cost = [i.findAll("span") for i in prd_cost]
    prd_cost = [i[1].text for i in prd_cost]

    prd_link = prd_list.findAll("div", {"class": "thumbnail"})
    prd_link = [main_url + i.find("a")['href'] for i in prd_link]

    prd_info = zip(prd_name, prd_cost, prd_link)

    for i in prd_info:
        print(i)


get_product_info(url)

# prd_list = bs_obj.select("ul.prdList div.box div.description p.name span")
# prd_cost = bs_obj.select("ul.prdList div.box div.description ul li span")

# for i in prd_list:
#     print(i.text)
#
# for i in prd_cost:
#     print(i.text)

