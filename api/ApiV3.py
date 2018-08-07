import requests

class SummonerApi():

    # Summoner related queries
    def get_summoner_by_account(self, summoner_account,region, api_key):
        url = 'https://'+region+'.api.riotgames.com/lol/summoner/v3/summoners/by-account/'+ \
              summoner_account +'?api_key='+ api_key
        r = requests.get(url)
        return r.json()

    def get_summoner_by_name(self, summoner_name,region, api_key):
        url = 'https://'+region+'.api.riotgames.com/lol/summoner/v3/summoners/by-name/'+\
              summoner_name +'?api_key='+ api_key
        r = requests.get(url)
        return r.json()

    def get_summoner_by_id(self, summoner_id,region, api_key):
        url = 'https://' + region + '.api.riotgames.com/lol/summoner/v3/summoners/' + \
              summoner_id + '?api_key=' + api_key
        r = requests.get(url)
        return r.json()

class LeaguesApi():

    def get_leagues_by_summoner_id(self, summoner_id,region, api_key):
        url = 'https://'+ region +'.api.riotgames.com//lol/league/v3/positions/by-summoner/'+ \
              summoner_id +'?api_key='+ api_key
        r = requests.get(url)
        return r.json()

class MatchesApi():

    def get_matchlist_by_account_id(self, account_id, begin_index, region, api_key, end_index = 0):
        if end_index == 0:
            url = 'https://' + region + '.api.riotgames.com/lol/match/v3/matchlists/by-account/' + \
                  str(account_id)+ '?beginIndex=' + str(begin_index) + '&api_key=' + api_key
        else:
            url = 'https://' + region + '.api.riotgames.com/lol/match/v3/matchlists/by-account/' + \
                  str(account_id) + '?beginIndex=' + str(begin_index) + '&endIndex='+str(end_index)+\
                  '&api_key=' + api_key
        r = requests.get(url)
        return r.json()
    def get_match_by_game_id(self,game_id,region, api_key):
        url = 'https://' + region + '.api.riotgames.com/lol/match/v3/matches/' + \
              str(game_id) + '?api_key=' + api_key
        r = requests.get(url)
        return r.json()

    def get_timeline_by_game_id(self,game_id,region,api_key):
        url = 'https://' + region + '.api.riotgames.com/lol/match/v3/timelines/by-match/' + \
              str(game_id) + '?api_key=' + api_key
        r = requests.get(url)

        return r.json()

class SpectatorApi():

    def get_active_game_by_summoner_id(self,summoner_id,region, api_key):
        url = 'https://' + region + '.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/' + \
              str(summoner_id) + '?api_key=' + api_key
        r = requests.get(url)
        return r.json()