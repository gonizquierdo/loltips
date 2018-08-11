from api.ApiConnector import ApiConnector
from helpers.PlayerBehavior import PlayerBehavior
from db.DbFunctions import MongoConnector
import json

def champion_name(champions, key):
    print(key)

with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)

with open(config['ROOT_DIR']+'/data/datadragon/8.14.1/data/es_MX/champion.json', encoding='utf8') as f:
        champions = json.load(f)

connector = ApiConnector(config['RIOT']['REGION'],config['RIOT']['API-KEY'])
db_connector = MongoConnector()
behavior_helper = PlayerBehavior()

summoner_name = 'Meisser'
summoner_lane = 'JUNGLE'    # TOP, JUNGLE, MID, BOTTOM
summoner = connector.get_summoner_by_name(summoner_name)
print(summoner)

gamelist = connector.get_last_games_by_account_id_for_lane(summoner['accountId'], summoner_lane)
game_count = 0
for game in gamelist:
    champion = db_connector.get_champion_by_id('champions',game['champion'])
    print('Champ: '+ champion['name'])
    full_game = connector.get_match_by_game_id(game['gameId'])

    if behavior_helper.is_roamer(connector,full_game,summoner_name):
        game_count += 1

if game_count > len(gamelist)/2:
    print("El jugador {} ha roameado exitosamente en {} de los ultimos {} juegos en {}. Sigue sus movimientos!".format(summoner_name, game_count, len(gamelist), summoner_lane))
else:
    print("El jugador {} ha roameado exitosamente en {} de los ultimos {} juegos en {}. No es muy peligroso.".format(summoner_name,
                                                                                                    game_count,
                                                                                                    len(gamelist),
                                                                                                    summoner_lane))
