from api.ApiConnector import ApiConnector
from helpers.PlayerBehavior import PlayerBehavior
import json, pprint
from riotwatcher import RiotWatcher

behavior_helper = PlayerBehavior()

with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)


connector = ApiConnector('la2', config['RIOT']['API-KEY'])
summoner = connector.get_summoner_by_name('Baqueta')

print(connector.get_summoner_league_and_division(summoner['id']))