

def get_summoner_kills_deaths_assists_for_match(connector, game_id, summoner_name):
    game = connector.get_match_by_game_id(game_id)

    for participant in game['participantIdentities']:
        if participant['player']['summonerName'] == summoner_name:
            summoner_id = participant['participantId']

    kills = game['participants'][summoner_id - 1]['stats']['kills']
    deaths = game['participants'][summoner_id - 1]['stats']['deaths']
    assists = game['participants'][summoner_id - 1]['stats']['assists']

    return kills, deaths, assists

def get_kda_for_match(game_id,summoner_name):
    kills, deaths, assists = get_summoner_kills_deaths_assists_for_match(game_id, summoner_name)

    return (kills+assists)/deaths if deaths > 0 else kills+assists

def get_summoner_kda_recent_matches(connector, summoner_name):
    summoner = connector.get_summoner_by_name(summoner_name)
    matchlist = connector.get_matchlist_by_account_id(summoner['accountId'])

    recent_matches_kda = {}
    for match in matchlist['matches']:
        game_id = match['gameId'];
        kda = get_kda_for_match(game_id,summoner_name)
        recent_matches_kda[game_id] = kda
    return recent_matches_kda

