import requests
from api.ApiV3 import SummonerApi, MatchesApi, LeaguesApi, SpectatorApi
from db.DbFunctions import MongoConnector

class ApiConnector():

    def __init__(self, region, api_key):
        self._db_connector = MongoConnector()
        self._api_key = api_key
        self._region = region
        self._initialize_apis()

    def _initialize_apis(self):
        self._summoner_api = SummonerApi()
        self._matches_api = MatchesApi()
        self._spectator_api = SpectatorApi()

    # ------ Summoner related functions ------
    def get_summoner_by_name(self, summoner_name):
        summoner = self._db_connector.get_summoner_by_name('summoners',summoner_name)
        if summoner:
            print('Got summoner from db')
            return summoner
        else:
            summoner = self._summoner_api.get_summoner_by_name(summoner_name, self._region, self._api_key)
            self._db_connector.save_summoner('summoners',summoner)
            print('Queried Riot for summoner')
            return summoner

    def get_matchlist_by_account_id(self, account_id):
        # Este método debería ir paginando y devolver una lista con todos los matches existentes. No me gusta mucho
        # como pagina ni lo que devuelve. Como la información de mas de 2000 games no es tan útil, recomiendo usar el
        # método de abajo especificando la cantidad de games que se quieren traer.

        #Edit: Creo que anda bastante para el culo. Ver denuevo.

        begin_index = 0
        matchlist = self._matches_api.get_matchlist_by_account_id(account_id, begin_index, self._region, self._api_key)
        matches = matchlist['matches']

        while matchlist['endIndex'] < matchlist['totalGames']:
            if begin_index+100 < matchlist['totalGames']:
                matchlist = self._matches_api.get_matchlist_by_account_id(account_id, begin_index, self._region,
                                                                    self._api_key)
                matches += matchlist['matches']
            else:
                matchlist = self._matches_api.get_matchlist_by_account_id(account_id,
                                                                     begin_index,
                                                                     self._region, self._api_key,
                                                                     end_index = matchlist['totalGames'])
                matches += matchlist['matches']

            begin_index = matchlist['endIndex'] + 1
        return matches

    def get_last_games_by_account_id(self,account_id, n_games=20):
        begin_index = 0
        if n_games < 100:
            return self._matches_api.get_matchlist_by_account_id(account_id, begin_index, self._region, self._api_key,
                                                                 n_games)['matches']
        else:
            print("MAX 100 GAMES.")

    def get_last_games_by_account_id_for_lane(self, account_id, lane, n_games=50):
        begin_index = 0
        if n_games < 100:

            matchlist =  self._matches_api.get_matchlist_by_account_id(account_id, begin_index, self._region, self._api_key,
                                                                 n_games)
            matches = []
            for game in matchlist['matches']:
                if game['lane'] == lane:
                    matches.append(game)
            return matches
        else:
            print("MAX 100 GAMES.")

    # ------ Matches related functions ------
    def get_match_by_game_id(self,game_id):
        return self._matches_api.get_match_by_game_id(game_id,self._region,self._api_key)

    def get_active_game_by_summoner_id(self,summoner_id):
        print(summoner_id)
        return self._spectator_api.get_active_game_by_summoner_id(summoner_id, self._region, self._api_key)

    def get_timeline_by_game_id(self, game_id):
        return self._matches_api.get_timeline_by_game_id(game_id, self._region, self._api_key)