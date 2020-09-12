from urllib.request import urlopen
import requests
import json

api_key = "RGAPI-c2bcd396-b898-4fb3-acaf-7ff35a7f6386"
summoner_name = "Hide on bush"

summoner = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name
params = {'api_key': api_key}
# input_data = {'summonerName': summoner_name}
r = requests.get(summoner, params=params)
summoner_id_info = r.json()

# print(summoner_id_info)

summoner_account_id = summoner_id_info['accountId']
matchlist = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + summoner_account_id
params = {'api_key': api_key}
r = requests.get(matchlist, params=params)
summoner_match_info = r.json()


def get_champion_simple_dict(url):
    text = urlopen(url)
    json_champion = json.load(text)

    champion_key_name_dict = dict()

    for champ_info in json_champion['data'].values():
        champion_key_name_dict[int(champ_info['key'])] = champ_info['name']

    return champion_key_name_dict


# print(summoner_match_info['matches'])
champion_json_url = "http://ddragon.leagueoflegends.com/cdn/9.24.2/data/ko_KR/champion.json"
champion_simple_dict = get_champion_simple_dict(champion_json_url)
# print(champion_simple_dict)

for champ in summoner_match_info['matches']:
    print(f"Play Champion : {champion_simple_dict[champ['champion']]}")

