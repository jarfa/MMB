import json

__author__ = 'Mike'

class PlayersLoader:
    pass

def get_all_players():
    with open('./jsonFile.json') as data_file:
        data = json.load(data_file)

    for player_name in data.keys():
        print player_name
        # print data[player_name]["p"]
        # print data[player_name]["b"]


