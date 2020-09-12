import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/listing/hk-eos/"


def get_bp_info(_url):
    result = requests.get(_url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    profile_name = bs_obj.find("div", {"class": "profile-name"})
    h1_bp_name = profile_name.find("h1")
    bp_name = h1_bp_name.text

    cover_buttons = bs_obj.find("div", {"class": "cover-buttons"})
    button_label = bs_obj.find("span", {"class": "button-label"})
    location = button_label.text

    # location = bs_obj.select("div.cover-buttons ul span.button-label")

    # link = location[1].find("a")['href']

    lis = cover_buttons.findAll("li")
    li_tag = lis[1]
    a_tag = li_tag.find("a")
    link = a_tag['href']

    dict1 = dict()
    dict1['name'] = bp_name
    dict1['location'] = location
    dict1['link'] = link

    return dict1


dict_result = get_bp_info(url)
print(dict_result)

mainpage_url = "https://bp.eosgo.io/"
result = requests.get(url=mainpage_url)
bs_obj = BeautifulSoup(result.content, "html.parser")

lf_items = bs_obj.findAll("div", {"class": "lf-item"})

hrefs = [div.find("a")['href'] for div in lf_items]

for number in range(5):
    dict_result = get_bp_info(hrefs[number])
    print(dict_result)

