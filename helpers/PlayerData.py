def get_summoner_kills_deaths_assists_for_match(connector, game_id, summoner_name):
    game = connector.get_match_by_game_id(game_id)

    for participant in game['participantIdentities']:
        if participant['player']['summonerName'] == summoner_name:
            summoner_id = participant['participantId']

    kills = game['participants'][summoner_id - 1]['stats']['kills']
    deaths = game['participants'][summoner_id - 1]['stats']['deaths']
    assists = game['participants'][summoner_id - 1]['stats']['assists']

    return kills, deaths, assists

def get_kda_for_match(connector, game_id,summoner_name):
    kills, deaths, assists = get_summoner_kills_deaths_assists_for_match(connector, game_id, summoner_name)

    return (kills+assists)/deaths if deaths > 0 else kills+assists

def get_summoner_kda_recent_matches(connector, summoner_name):
    summoner = connector.get_summoner_by_name(summoner_name)
    matchlist = connector.get_matchlist_by_account_id(summoner['accountId'])

    recent_matches_kda = {}
    for match in matchlist['matches']:
        game_id = match['gameId'];
        kda = get_kda_for_match(connector,game_id,summoner_name)
        recent_matches_kda[game_id] = kda
    return recent_matches_kda

def get_summoner_vision_score_for_match(connector, game_id,summoner_name):
    game = connector.get_match_by_game_id(game_id)
    for participant in game['participantIdentities']:
        if participant['player']['summonerName'] == summoner_name:
            summoner_id = participant['participantId']

    vision_score = game['participants'][summoner_id - 1]['stats']['visionScore']

    return vision_score

def get_summoner_gpm_for_match(connector, game_id,summoner_name):
    game = connector.get_match_by_game_id(game_id)

    for participant in game['participantIdentities']:
        if participant['player']['summonerName'] == summoner_name:
            summoner_id = participant['participantId']

    game_duration = round(game['gameDuration']/60)
    gold_earned = game['participants'][summoner_id - 1]['stats']['goldEarned']

    gpm = gold_earned/game_duration
    return gpm

def get_summoner_cspm_for_match(connector, game_id,summoner_name):
    game = connector.get_match_by_game_id(game_id)

    for participant in game['participantIdentities']:
        if participant['player']['summonerName'] == summoner_name:
            summoner_id = participant['participantId']

    game_duration = round(game['gameDuration']/60)
    minions_killed = game['participants'][summoner_id - 1]['stats']['totalMinionsKilled']
    cspm = minions_killed / game_duration
    return cspm

def get_summoner_dmgpm_to_champions_for_match(connector, game_id,summoner_name):
    game = connector.get_match_by_game_id(game_id)

    for participant in game['participantIdentities']:
        if participant['player']['summonerName'] == summoner_name:
            summoner_id = participant['participantId']

    game_duration = round(game['gameDuration'] / 60)
    damage_to_champions = game['participants'][summoner_id - 1]['stats']['totalDamageDealtToChampions']
    dmgpm_to_champions = damage_to_champions / game_duration
    return dmgpm_to_champions
