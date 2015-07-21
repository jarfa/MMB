__author__ = 'Mike'

# anchor extraction from html document
import urllib2
import re
import json

from bs4 import BeautifulSoup

import Player


class FanDuelScraper:

    def __init__(self, fan_duel_game_url):
        self.fan_duel_game_url = fan_duel_game_url

    def get_fan_duel_players(self):
        webpage = urllib2.urlopen(self.fan_duel_game_url)
        soup = BeautifulSoup(webpage)
        script = soup.find('script', text=re.compile('FD\.playerpicker\.allPlayersFullData'))

        json_text = re.search(r'^\s*FD\.playerpicker\.allPlayersFullData\s*=\s*({.*?})\s*;\s*$',
                              script.string, flags=re.DOTALL | re.MULTILINE).group(1)

        data = json.loads(json_text)


        print json.dumps(data,indent=1)


        fan_duel_players = list()
        for fan_duel_id in data.keys():

            position = data[fan_duel_id][0]
            name = data[fan_duel_id][1]
            team_number = data[fan_duel_id][2]
            fan_duel_cost = data[fan_duel_id][5]
            fan_duel_fppg = data[fan_duel_id][6]
            injury_suspension_string = data[fan_duel_id][12]

            injury_suspension_status = 0
            if injury_suspension_string != "":
                injury_suspension_status = 1
            player = Player(name, position, team_number, fan_duel_id, fan_duel_cost, fan_duel_fppg, injury_suspension_status)

            fan_duel_players.append(player)

        return fan_duel_players





