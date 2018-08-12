from flask import Flask, Response
from flask_cors import CORS

from api.ApiConnector import ApiConnector
from helpers.PlayerBehavior import PlayerBehavior
from helpers.MapFunctions import MapFunctions
import json, time

app = Flask(__name__)

@app.route("/active-game/<summoner_name>", methods=['GET', 'POST'])
def main(summoner_name):
    summoner = connector.get_summoner_by_name(summoner_name)
    response = {}
    start_time = time.time()
    print("Incoming request")
    n_games, roam_games = behavior_helper.get_roamer_for_last_games(connector,summoner_name)
    print("T: " + str(time.time() - start_time))
    return Response(json.dumps({"nGames":n_games, "roamedGames":roam_games}, indent=4))

if __name__ == "__main__":
    behavior_helper = PlayerBehavior()
    map_helper = MapFunctions()

    with open('api/config.json') as json_data_file:
        config = json.load(json_data_file)

    connector = ApiConnector(config['RIOT']['REGION'], config['RIOT']['API-KEY'])
    CORS(app)

    app.run(debug=True, host='192.168.0.19')