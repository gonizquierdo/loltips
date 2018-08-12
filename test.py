from api.ApiConnector import ApiConnector
from helpers.PlayerBehavior import PlayerBehavior
from helpers.MapFunctions import MapFunctions
import json, pprint

behavior_helper = PlayerBehavior()
map_helper = MapFunctions()

with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)
print(config)

connector = ApiConnector(config['RIOT']['REGION'],config['RIOT']['API-KEY'])

summoner_name = 'WatchLeo'
summoner = connector.get_summoner_by_name(summoner_name)

active_game = connector.get_active_game_by_summoner_id(summoner['id'])

for summoner in active_game['participants']:
    behavior_helper.get_roamer_for_last_games(connector,summoner['summonerName'])
print(active_game)
