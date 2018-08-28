from api.ApiConnector import ApiConnector
from helpers.PlayerBehavior import PlayerBehavior
import json, pprint
from riotwatcher import RiotWatcher

behavior_helper = PlayerBehavior()

with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)


connector = ApiConnector('la2', config['RIOT']['API-KEY'])
print(connector.get_summoner_by_name('Gonzus'))