import helpers.PlayerData as player_data
import json


class PlayerBehavior:

    def __init__(self):
        #self._map_helper = MapFunctions()
        pass

    """
      def is_roamer(self, connector, game, summoner_name):
      
        roamer = False
        for participant_identity in game['participantIdentities']:
            if participant_identity['player']['summonerName'] == summoner_name:
                participant_id = participant_identity['participantId']

        summoner = game['participants'][participant_id - 1]
        summoner_lane = summoner['timeline']['lane']

        if summoner_lane != 'JUNGLE':

            timeline = connector.get_timeline_by_game_id(game['gameId'])
            for frame in timeline['frames']:
                events = frame['events']
                for event in events:
                    if event['type'] == 'CHAMPION_KILL' and (
                            event['killerId'] == participant_id or participant_id in event['assistingParticipantIds']):

                        place = \
                        self._map_helper.get_map_sector_by_xy(event['position']['x'], event['position']['y']).split(
                            '_')[0]
                        event_time_min = event['timestamp'] / 60000
                        if place != summoner_lane and event_time_min < 10:
                            roamer = True
                            break
        return roamer

    def get_roamer_for_last_games(self, connector, summoner_name):
        summoner = connector.get_summoner_by_name(summoner_name)
        gamelist = connector.get_last_games_by_account_id(summoner['accountId'])
        count = 0
        for game in gamelist:
            full_game = connector.get_match_by_game_id(game['gameId'])
            if self.is_roamer(connector, full_game, summoner_name):
                count += 1

        return len(gamelist), count
    """

    def get_stats_for_matchlist(self, connector, summoner, gamelist):
        stats = {}
        n_games = 0
        avg_kda = 0
        avg_vision_score = 0
        avg_gpm = 0
        avg_cspm = 0
        avg_dmgpm_to_champions = 0

        for game in gamelist:
            # Normal Games only.
            if game['queue'] in [420,430]:
                n_games += 1
                avg_kda += player_data.get_kda_for_match(connector, game['gameId'], summoner['name'])
                avg_vision_score += player_data.get_summoner_vision_score_for_match(connector, game['gameId'],
                                                                                    summoner['name'])
                avg_gpm += player_data.get_summoner_gpm_for_match(connector, game['gameId'], summoner['name'])
                avg_cspm += player_data.get_summoner_cspm_for_match(connector, game['gameId'], summoner['name'])
                avg_dmgpm_to_champions +=  player_data.get_summoner_dmgpm_to_champions_for_match(connector, game['gameId'], summoner['name'])

        stats['n_games'] = n_games;
        stats['avg_kda'] = round(avg_kda / n_games, 2)
        stats['avg_vision_score'] = round(avg_vision_score / n_games, 2)
        stats['avg_gpm'] = round(avg_gpm / n_games, 2)
        stats['avg_cspm'] = round(avg_cspm / n_games, 2)
        stats['avg_dmgpm_to_champions'] = round(avg_dmgpm_to_champions / n_games, 2)


        return stats
