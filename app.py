from flask import Flask, Response
from flask_cors import CORS

from api.ApiConnector import ApiConnector
from helpers.PlayerBehavior import PlayerBehavior
import json, time, os

app = Flask(__name__)
CORS(app)

behavior_helper = PlayerBehavior()
with open('api/config.json') as json_data_file:
    config = json.load(json_data_file)

connector = ApiConnector(config['RIOT']['REGION'], config['RIOT']['API-KEY'])

@app.route("/")
def main():
    return "/stats/summoner_name for stats"

@app.route("/active-game/<summoner_name>", methods=['GET', 'POST'])
def active_game_by_summoner_name(summoner_name):
    summoner = connector.get_summoner_by_name(summoner_name)
    response = {}
    print("Incoming request")
    n_games, roam_games = behavior_helper.get_roamer_for_last_games(connector,summoner_name)
    return Response(json.dumps({"nGames":n_games, "roamedGames":roam_games}, indent=4))

@app.route("/stats/<summoner_name>", methods=['GET','POST'])
def stats_game_by_summoner_name(summoner_name):
    summoner = connector.get_summoner_by_name(summoner_name)

    matchlist =  connector.get_last_games_by_account_id(summoner['accountId'])
    stats = behavior_helper.get_stats_for_matchlist(connector, summoner, matchlist)

    stats['summoner_name'] = summoner_name
    stats['summoner_level'] = summoner['summonerLevel']
    stats['summoner_icon'] = summoner['profileIconId']
    stats['summoner_league'] = connector.get_summoner_league_and_division(summoner['id'])
    return Response(json.dumps(stats))

if __name__ == "__main__":
    app.run()