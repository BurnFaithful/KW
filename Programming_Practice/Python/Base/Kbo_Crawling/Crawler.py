from bs4 import BeautifulSoup
import requests

def year_select(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')

    year = soup.select('select.select03 > option')
    for row in year:
        print(row.text)

    print(year)

    req.close()

def crawling(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')

    table_attribute = soup.select('table > thead > tr > th')
    for row in table_attribute:
        print(f"{row.text:^5}", end='\t')
    # table_data = soup.select('.tData01 tt')
    print()

    degree = len(table_attribute)
    table_data = soup.select('table > tbody > tr > td')
    for index, row in enumerate(table_data):
        if index % degree == 0:
            print()
        print(f"{row.text:^5}", end='\t')

    req.close()

if __name__ == "__main__":
    url = "https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx"
    year_select(url)
    # crawling(url)