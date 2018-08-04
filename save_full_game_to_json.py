from api.ApiConnector import ApiConnector
import json

connector = ApiConnector('la2','RGAPI-4cd8dfe2-215d-48f4-8500-2047e1e26ded')

ouput_dir = 'D:/Documents/Coding/loltips/data/outputs/sample_full_games/'
game_id= 290371794

full_game = connector.get_match_by_game_id(game_id)
file = open(ouput_dir+str(game_id)+'_full_game.json','w')
file.write(json.dumps(full_game, indent=4, sort_keys=True))
file.close()