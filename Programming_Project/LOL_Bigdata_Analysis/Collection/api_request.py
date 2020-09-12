from urllib.request import urlopen
import time
import requests
import json

api_key = "RGAPI-9062f892-a71f-4aa9-af0c-2d44d1e16540"
champion_json = "http://ddragon.leagueoflegends.com/cdn/9.24.2/data/ko_KR/champion.json"

def get_api_key(): # 추후 처리
    return api_key


def get_summoner_info(summoner_name):
    summoner = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
    params = {'api_key': api_key}
    req = requests.get(summoner, params=params)

    return req.json()


def get_matchlist_info_by_summoner(summoner_name):
    summoner_accountid = get_summoner_info(summoner_name)['accountId']

    matchlist = f'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/{summoner_accountid}'
    params = {'api_key': api_key}
    req = requests.get(matchlist, params=params)
    
    return req.json()


def get_match_info_by_matchid(match_id):
    match = f'https://kr.api.riotgames.com/lol/match/v4/matches/{match_id}'
    params = {'api_key': api_key}
    req = requests.get(match, params=params)

    return req.json()


def get_match_timeline_info_by_matchid(match_id):
    match_timeline = f'https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/{match_id}'
    params = {'api_key': api_key}
    req = requests.get(match_timeline, params=params)

    return req.json()


def get_champion_id_name_dict():
    text = urlopen(champion_json)
    json_champion = json.load(text)
    champion_id_name_dict = dict()

    for champ_info in json_champion['data'].values():
        champion_id_name_dict[int(champ_info['key'])] = champ_info['name']

    return champion_id_name_dict


summoner_matchlist = get_matchlist_info_by_summoner("Assault")['matches']
for match in summoner_matchlist:
    # print(get_match_info_by_matchid(match['gameId']))
    print(get_match_timeline_info_by_matchid(match['gameId']))
    time.sleep(1)
# summoner_match_info = get_matchlist_info_by_summoner("Assault")
# champion_id_name_dict = get_champion_id_name_dict()
# for champ in summoner_match_info['matches']:
#     print(f"Play Champion : {champion_id_name_dict[champ['champion']]}")

