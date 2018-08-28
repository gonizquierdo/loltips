from api.ApiConnector import ApiConnector
import json

with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)
print(config)

connector = ApiConnector(config['RIOT']['REGION'],config['RIOT']['API-KEY'])


ouput_dir = 'D:/Documents/Coding/loltips/data/outputs/sample_full_games/'
game_id= 603569718

full_game = connector.get_match_by_game_id(game_id)
file = open(ouput_dir+str(game_id)+'_full_game.json','w')
file.write(json.dumps(full_game, indent=4, sort_keys=True))
file.close()