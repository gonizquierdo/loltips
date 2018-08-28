from pymongo import MongoClient
import json, os

class MongoConnector:

    def __init__(self):
        path = os.path.abspath(__file__)
        with open('api/config.json') as json_data_file:
            config = json.load(json_data_file)

        self._client = MongoClient('mongodb://{}:{}@{}:{}/{}'.format(config['DB']['USER'], config['DB']['PASSWORD'],
                                                                     config['DB']['HOST'], config['DB']['PORT'],
                                                                     config['DB']['DB_NAME']))
        self._db = self._client['lol-tips']

    def insert_one(self, collection_name, document):
        collection = self._db[collection_name]
        collection.insert_one(document)

    def insert_many(self, collection_name, documents):
        collection = self._db[collection_name]
        collection.insert_many(documents)

    def get_document_by_id(self, collection_name, document_id):
        collection = self._db[collection_name]
        return collection.find_one(document_id)

    # ------ League related queries -------
    def get_game_by_game_id(self,collection_name, game_id):
        collection = self._db[collection_name]
        return collection.find_one({'gameId':game_id})

    def save_game(self, collection_name, game):
        collection = self._db[collection_name]
        collection.insert_one(game)

    def get_summoner_by_name(self, collection_name, summoner_name):
        collection = self._db[collection_name]
        return collection.find_one({'name':summoner_name})

    def save_summoner(self, collection_name, summoner):
        collection = self._db[collection_name]
        collection.insert_one(summoner)

    def save_champion_list(self, collection_name, champion_list):
        self.insert_many(collection_name, champion_list)

    def get_champion_by_id(self, collection_name, champion_id):
        collection = self._db[collection_name]
        return collection.find_one({'key':str(champion_id)})

    def get_timeline_by_game_id(self,collection_name, game_id):
        collection = self._db[collection_name]
        return collection.find_one({'gameId':game_id})

    def save_timeline(self, collection_name, timeline, game_id):
        collection = self._db[collection_name]
        timeline['gameId'] = game_id
        collection.insert_one(timeline)