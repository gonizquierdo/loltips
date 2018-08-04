from api.ApiConnector import ApiConnector
import json, pprint

connector = ApiConnector('la2','RGAPI-fa217bbb-2ae1-4869-b368-0bc4cb4576af')

ouput_dir = 'D:/Documents/Coding/loltips/data/outputs/sample_full_games/'

with open(ouput_dir+'/290371794_full_game.json') as f:
    data = json.load(f)


for participant in data['participants']:
    print(json.dumps(participant, indent=4, sort_keys=True))


