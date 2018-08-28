import json
from db.DbFunctions import MongoConnector

db_connector = MongoConnector()
with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)

with open(config['ROOT_DIR'] + '/data/datadragon/8.14.1/data/es_MX/champion.json', encoding='utf8') as f:
    champions = json.load(f)

champion_list = []
for champion in champions['data']:
    champion_list.append(champions['data'][champion])

db_connector.save_champion_list('champions', champion_list)