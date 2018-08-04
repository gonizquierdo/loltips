from api.ApiConnector import ApiConnector
import json

connector = ApiConnector('la2','RGAPI-4cd8dfe2-215d-48f4-8500-2047e1e26ded')

summoner = connector.get_summoner_by_name('Gonzus')
print(summoner)

connector.get_matchlist_by_account_id(summoner['accountId'])
