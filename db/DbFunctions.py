from pymongo import MongoClient

class MongoConnector:

    def __init__(self):
        self._client = MongoClient('mongodb://localhost:27017/')
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

    def get_summoner_by_name(self, collection_name, summoner_name):
        collection = self._db[collection_name]
        return collection.find_one({'name':summoner_name})

    def save_summoner(self, collection_name, summoner):
        collection = self._db[collection_name]
        collection.insert_one(summoner)

    def save_champion_list(self, collection_name, champion_list):
        self.insert_many(collection_name, champion_list)