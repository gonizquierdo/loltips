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

ouput_dir = 'D:/Documents/Coding/loltips/data/outputs/sample_full_games/'

with open(ouput_dir+'/603569718_full_game.json') as f:
    data = json.load(f)


roamer = behavior_helper.is_roamer(connector,data,'Gonzus')
