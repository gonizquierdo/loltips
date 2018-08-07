from api.ApiConnector import ApiConnector
from helpers.PlayerBehavior import PlayerBehavior
import json

with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)

connector = ApiConnector(config['RIOT']['REGION'],config['RIOT']['API-KEY'])
behavior_helper = PlayerBehavior()

summoner_name = 'Muscle Reformed'
summoner = connector.get_summoner_by_name(summoner_name)
print(summoner)

gamelist = connector.get_last_games_by_account_id(summoner['accountId'])
game_count = 0
for game in gamelist:
    print(gamelist)
    full_game = connector.get_match_by_game_id(game['gameId'])
    if behavior_helper.is_roamer(connector,full_game,summoner_name):
        game_count += 1

if game_count > len(gamelist)/2:
    print("El jugador {} ha roameado en {} de los ultimos {} juegos. Sigue sus movimientos!".format(summoner_name, game_count, len(gamelist)))
else:
    print("El jugador {} ha roameado en {} de los ultimos {} juegos. Meh, no le des bola.".format(summoner_name,
                                                                                                    game_count,
                                                                                                    len(gamelist)))
