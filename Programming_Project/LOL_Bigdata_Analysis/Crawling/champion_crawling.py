import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver_path = "D:/Download/chromedriver_win32/chromedriver.exe"
# driver_options = webdriver.ChromeOptions()
# driver_options.add_argument('headless')

driver = webdriver.Chrome(executable_path=driver_path)

tierlist_url = "https://u.gg/lol/tier-list"
combat_url = "https://u.gg/lol/combat"
objective_url = "https://u.gg/lol/objective"
# driver.get(main_url)


def get_tierlist_page_source(close=True, rank='overall', region='kr'):
    driver.get(f'{tierlist_url}?rank={rank}&region={region}')
    # element = driver.find_element_by_css_selector("div.rank-option > span")
    # driver.execute_script(f"arguments[0].innerHTML = '{rank}';", element)
    # element = driver.find_element_by_css_selector("div.region-option > span")
    # driver.execute_script(f"arguments[0].innerHTML = '{region}';", element)
    element = driver.find_element_by_tag_name("body")

    for _ in range(15):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    # if close:
    #     driver.close()

    return driver.page_source


def get_combat_page_source(close=True, rank='overall', region='kr'):
    driver.get(f'{combat_url}?rank={rank}&region={region}')
    element = driver.find_element_by_tag_name('body')

    for _ in range(15):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    return driver.page_source


def get_tierlist_page():
    return BeautifulSoup(get_tierlist_page_source(), "html.parser")


def get_combat_page():
    return BeautifulSoup(get_combat_page_source(), "html.parser")


def get_tierlist_winrate_sorted_data():
    tierlist_page = get_tierlist_page()

    return tierlist_page.select('div.rt-tbody div.rt-tr-group div.rt-td.winrate.highlight > span > b')


def get_tierlist_rate_data():
    tierlist_page = get_tierlist_page()

    rate_data_list = list()

    tr_group = tierlist_page.select('div.rt-tbody div.rt-tr-group')
    for tr in tr_group:
        champ_name = tr.select_one('div.rt-td.champion strong')
        winrate = tr.select_one('div.rt-td.winrate.highlight > span > b')
        pickrate = tr.select_one('div.rt-td.pickrate > span')
        banrate = tr.select_one('div.rt-td.banrate > span')
        rate_data = zip(champ_name, winrate, pickrate, banrate)
        rate_data_list.append(rate_data)

    return rate_data_list


def get_combat_data():
    combat_page = get_combat_page()

    combat_data_list = list()

    tr_group = combat_page.select('div.rt-tbody div.rt-tr-group')
    for tr in tr_group:
        champ_name = tr.select_one('div.rt-td.champion strong')
        datas = tr.select('div.rt-td > span')
        for data in datas:
            print(data.text)
        combat_data = zip(champ_name, datas)
        combat_data_list.append(combat_data)

    return combat_data_list


if __name__ == "__main__":
    # print(get_tierlist_data())
    # print(get_tierlist_winrate_sorted_data())
    # winrate_data_list = get_tierlist_winrate_sorted_data()
    # for i, winrate_data in enumerate(winrate_data_list):
        # print(i, ":", winrate_data.text)
    # rate_data_list = get_tierlist_rate_data()
    # for i, rate_data in enumerate(rate_data_list):
    #     for data in rate_data:
    #         print(f'{i + 1} : {data}', end='')
    #     print()
    
    # combat_data_list = get_combat_data()
    # for i, combat_data in enumerate(combat_data_list):
    #     for data in combat_data:
    #         print(f'{i + 1} : {data}', end='')
    #     print()
    get_combat_data()