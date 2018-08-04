from api.ApiConnector import ApiConnector
import json

connector = ApiConnector('la2','RGAPI-fa217bbb-2ae1-4869-b368-0bc4cb4576af')

ouput_dir = 'D:/Documents/Coding/loltips/data/outputs/sample_spectator_games/'
summoner_name = 'Meisser'

summoner = connector.get_summoner_by_name(summoner_name)
active_game = connector.get_active_game_by_summoner_id(summoner['id'])
file = open(ouput_dir+str(summoner['id'])+'_game.json','w')
file.write(json.dumps(active_game, indent=4, sort_keys=True))
file.close()