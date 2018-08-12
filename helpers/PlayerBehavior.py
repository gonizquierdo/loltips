from helpers.MapFunctions import MapFunctions
import time
class PlayerBehavior:

    def __init__(self):
        self._map_helper = MapFunctions()

    def is_roamer(self,connector, game,summoner_name):
        """
        :param game: Full Game
        :param summoner_name: Summoner Name
        :return: True if summoner killed or assisted while roaming.
        """
        roamer = False
        for participant_identity in game['participantIdentities']:
            if participant_identity['player']['summonerName'] == summoner_name:
                participant_id = participant_identity['participantId']

        summoner = game['participants'][participant_id-1]
        summoner_lane = summoner['timeline']['lane']

        if summoner_lane != 'JUNGLE':

            timeline = connector.get_timeline_by_game_id(game['gameId'])
            for frame in timeline['frames']:
                events = frame['events']
                for event in events:
                    if event['type'] == 'CHAMPION_KILL' and (event['killerId'] == participant_id or participant_id in event['assistingParticipantIds']):

                        place = self._map_helper.get_map_sector_by_xy(event['position']['x'],event['position']['y']).split('_')[0]
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
            if self.is_roamer(connector,full_game, summoner_name):
                count += 1

        return len(gamelist), count