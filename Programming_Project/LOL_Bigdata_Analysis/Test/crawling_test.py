import requests
from bs4 import BeautifulSoup

main_url = "https://www.op.gg"
champion_page_url = main_url + "/champion/statistics"
get_req_result = requests.get(champion_page_url)

bs_obj = BeautifulSoup(get_req_result.content, "html.parser")
# print(bs_obj)

champion_list_div = bs_obj.find("div", {"class": "champion-index__champion-list"})
# print(champion_list_div)

champion_data_link = champion_list_div.select("div > a")
for i in champion_data_link:
    # print(i['href'])
    get_req_champion_ana_page = requests.get(main_url + i['href'])
    bs_obj = BeautifulSoup(get_req_champion_ana_page.content, "html.parser")
    # print(bs_obj)
    champion_menu_tab = bs_obj.find("ul", {"class": "champion-stats-menu__list"})
    champion_counter = champion_menu_tab.find("li", {"data-tab-show-class": "championLayout-matchup"})
    print(champion_counter.find("a")['href'])
    champion_matchup_list_page = main_url + champion_counter.find("a")['href']
    get_req_champion_matchup_page = requests.get(champion_matchup_list_page)
    bs_obj = BeautifulSoup(get_req_champion_matchup_page.content, "html.parser")

    champion_matchup_champion_list = bs_obj.find("div", {"class": "champion-matchup-champion-list"})
    champion_matchup_champion = champion_matchup_champion_list.findAll("div", {"class": "champion-matchup-list__champion"})
    for j in champion_matchup_champion:
        champion_matchup_champion_name = j.find("span").text
        champion_matchup_champion_winrate = j.find("span", {"class": "champion-matchup-list__winrate"}).text
        print("vs " + champion_matchup_champion_name + " : " + champion_matchup_champion_winrate.strip())
# print(champion_data_link)