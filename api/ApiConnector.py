import requests
from riotwatcher import RiotWatcher
from db.DbFunctions import MongoConnector

class ApiConnector():

    def __init__(self, region, api_key):
        self._db_connector = MongoConnector()
        self._region = region
        self._watcher = RiotWatcher(api_key)

    # ------ Summoner related functions ------
    def get_summoner_by_name(self, summoner_name):
        summoner = self._db_connector.get_summoner_by_name('summoners',summoner_name)
        if not summoner:
            summoner = self._watcher.summoner.by_name(self._region, summoner_name)
            self._db_connector.save_summoner('summoners',summoner)
        return summoner


    def get_last_games_by_account_id(self,account_id, n_games=50):
        begin_index = 0

        if n_games < 100:
            return self._watcher.match.matchlist_by_account(self._region, account_id, end_index=n_games)['matches']
        else:
            print("MAX 100 GAMES.")

    def get_last_games_by_account_id_for_lane(self, account_id, lane, n_games=50):
        begin_index = 0
        if n_games < 100:

            matchlist =  self._watcher.match.matchlist_by_account(self._region, account_id, end_index=n_games)
            matches = []
            for game in matchlist['matches']:
                if game['lane'] == lane:
                    matches.append(game)
            return matches
        else:
            print("MAX 100 GAMES.")

    def get_summoner_league_and_division(self,summoner_id):
        res = self._watcher.league.positions_by_summoner(self._region, summoner_id)
        print(res)
        if res:
            for queue in res:
                if queue['queueType'] == 'RANKED_SOLO_5x5':
                    tier = queue['tier']
                    rank = queue['rank']
            return tier, rank
        else:
            return ["UNRANKED", "-"]

    # ------ Matches related functions ------
    def get_match_by_game_id(self,game_id):
        game = self._db_connector.get_game_by_game_id('matches', game_id)
        if game:
            return game
        else:
            game = self._watcher.match.by_id(self._region, game_id)
            self._db_connector.save_game('matches', game)
            return game

    def get_active_game_by_summoner_id(self,summoner_id):
        print(summoner_id)
        return self._watcher.spectator.by_summoner(self._region, summoner_id)

    def get_timeline_by_game_id(self, game_id):
        timeline = self._db_connector.get_timeline_by_game_id('timelines', game_id)
        if timeline:
            return timeline
        else:
            timeline = self._watcher.match.timeline_by_match(self._region, game_id)
            self._db_connector.save_timeline('timelines', timeline, game_id)
            return timeline

