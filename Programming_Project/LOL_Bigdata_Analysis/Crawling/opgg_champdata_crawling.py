import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver_path = "D:/Download/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)

champion_json = "http://ddragon.leagueoflegends.com/cdn/9.24.2/data/ko_KR/champion.json"
opgg_champ_stat_url = 'https://www.op.gg/champion/statistics'


def get_tierlist_page_source(close=True):
    driver.get(opgg_champ_stat_url)

    return driver.page_source


def get_tierlist_page():
    return BeautifulSoup(get_tierlist_page_source(), 'html.parser')


def get_champ_rate_data():
    tierlist_page = get_tierlist_page()

    rate_data_list = list()
    tr_group = tierlist_page.select('table.champion-index-table.tabItems > tbody > tr')
    for tr in tr_group:
        champ_name = tr.select('td')[3]
        winrate = tr.select('td')[4]
        pickrate = tr.select('td')[5]
        rate_data = zip(champ_name, winrate, pickrate)
        rate_data_list.append(rate_data)
    
    return rate_data_list


if __name__ == '__main__':
    # print(get_tierlist_page())
    rate_data_list = get_champ_rate_data()
    for rate_data in rate_data_list:
        for data in rate_data:
            print(data)