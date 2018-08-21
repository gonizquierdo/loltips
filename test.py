from api.ApiConnector import ApiConnector
from helpers.PlayerBehavior import PlayerBehavior
from helpers.MapFunctions import MapFunctions
import json, pprint
from riotwatcher import RiotWatcher

behavior_helper = PlayerBehavior()
map_helper = MapFunctions()

with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)


watcher = RiotWatcher(config['RIOT']['API-KEY'])
for i in range(1,200):
    print(watcher.summoner.by_name('la2','Gonzus'))