from Player.Player import Player

__author__ = 'Mike'

# anchor extraction from html document
from bs4 import BeautifulSoup
import urllib2
import re
import json

fan_duel_game_url = 'https://www.fanduel.com/e/Game/12662'


webpage = urllib2.urlopen(fan_duel_game_url)
soup = BeautifulSoup(webpage)
script = soup.find('script', text=re.compile('FD\.playerpicker\.allPlayersFullData'))

json_text = re.search(r'^\s*FD\.playerpicker\.allPlayersFullData\s*=\s*({.*?})\s*;\s*$',
                      script.string, flags=re.DOTALL | re.MULTILINE).group(1)

data = json.loads(json_text)


# print json.dumps(data,indent=1)


fan_duel_players = list()
for fan_duel_id in data.keys():

    position = data[fan_duel_id][0]
    name = data[fan_duel_id][1]
    team_number = data[fan_duel_id][2]
    fan_duel_cost = data[fan_duel_id][5]
    fan_duel_fppg = data[fan_duel_id][6]

    player = Player(name, position, team_number, fan_duel_id, fan_duel_cost, fan_duel_fppg)

    fan_duel_players.append(player)

print fan_duel_players.__sizeof__()

for player in fan_duel_players:
    player.print_player()





