from api.ApiConnector import ApiConnector
from db.DbFunctions import MongoConnector
import json

with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)


api_connector = ApiConnector(config['RIOT']['REGION'],config['RIOT']['API-KEY'])

base_summoner_name = 'Muscle Reformed'
base_summoner, base_source = api_connector.get_summoner_by_name(base_summoner_name)
base_gamelist = api_connector.get_last_games_by_account_id(base_summoner['accountId'])

for game in base_gamelist:
    full_game = api_connector.get_match_by_game_id(game['gameId'])
    participantIdentities = full_game['participantIdentities']
    for identity in participantIdentities:
        summoner, source = api_connector.get_summoner_by_name(identity['player']['summonerName'])
        print(source)
        gamelist = api_connector.get_last_games_by_account_id(summoner['accountId'])
        for game in gamelist:
            full_game = api_connector.get_match_by_game_id(game['gameId'])
            participantIdentities = full_game['participantIdentities']
            for identity in participantIdentities:
                try:
                    summoner, source = api_connector.get_summoner_by_name(identity['player']['summonerName'])
                except Exception as e:
                    print(e)

                print(source)



