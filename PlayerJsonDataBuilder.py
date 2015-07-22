from lxml import html
import requests
import Player
import json
import FanDuelScraper

class PlayerJsonBuilder():

    @staticmethod
    def getBatterUrl(player):
        return PlayerJsonBuilder.getUrl(player, "&t=b")

    @staticmethod
    def getPitcherUrl(player):
        return PlayerJsonBuilder.getUrl(player, "&t=p")

    @staticmethod
    def getUrl(player, substr):
        lastName = player.getLastName().lower()
        first_name_substr = player.getFirstName()[:2].lower()
        num = '01'
        if(", jr." in lastName):
            last_name_substr = lastName.replace(", jr.", "")[:5]
            num = '02'
        else:
            last_name_substr = lastName[:5]
        return 'http://www.baseball-reference.com/players/gl.cgi?id=' + last_name_substr + first_name_substr + num + substr + '&year=2015'

    @staticmethod
    def getBatterJson(player):
        page = requests.get(PlayerJsonBuilder.getBatterUrl(player))
        tree = html.fromstring(page.text)
        stuff = tree.xpath('//tr[contains(@id,"batting_gamelogs")]')
        currentScore = 0
        iteration=0
        yearsData = []
        for i in reversed(stuff):
            data={}
            date = i.findtext('.//td[4]/a')
            data['date'] = date

            opp = i.findtext('.//td[7]/a')
            data['opp'] = opp

            hits = int(i.findtext('.//td[13]'))
            data['hits'] = hits

            twoB = int(i.findtext('.//td[14]'))
            data['twoB'] = twoB

            threeB = int(i.findtext('.//td[15]'))
            data['threeB'] = threeB

            hr = int(i.findtext('.//td[16]'))
            data['hr'] = hr

            rbi = int(i.findtext('.//td[17]'))
            data['rbi'] = rbi

            runs = int(i.findtext('.//td[12]'))
            data['runs'] = runs

            bb = int(i.findtext('.//td[18]'))
            data['bb'] = bb

            sb = int(i.findtext('.//td[26]'))
            data['sb'] = sb

            hbp = int(i.findtext('.//td[21]'))
            data['hbp'] = hbp

            atBats = int(i.findtext('.//td[11]'))
            data['atBats'] = atBats

            outs = atBats - hits
            data['outs'] = outs

            scoreThatGame = hits + 2*twoB + 3*threeB + 4*hr + rbi + runs + bb + 2*sb + hbp - outs/float(4)
            data['scoreThatGame'] = scoreThatGame

            yearsData.append(data)

        return yearsData

    @staticmethod
    def getPitcherJson(player):
        page = requests.get(PlayerJsonBuilder.getPitcherUrl(player))
        tree = html.fromstring(page.text)
        stuff = tree.xpath('//tr[contains(@id,"pitching_gamelogs")]')
        currentScore = 0
        iteration=0
        yearsData = []
        for i in reversed(stuff):
            data = {}
            date = i.findtext('.//td[4]/a')
            data['date'] = date

            opp = i.findtext('.//td[7]/a')
            data['opp'] = opp
            
            result = i.findtext('.//td[8]')
            win = (result[:1] == 'W')
            data['win'] = win

            ip = PlayerJsonBuilder.fixUpInningsPitched(i.findtext('.//td[12]/span').strip()) #they do x.1 and x.2 for outs and we need x.33 and x.66
            data['ip'] = ip
            so = int(i.findtext('.//td[17]'))
            data['so'] = so
            er = int(i.findtext('.//td[15]'))
            data['er'] = er

            scoreThatGame = 0
            if(win):
                scoreThatGame = 4
            scoreThatGame += ip + so - er
            data['scoreThatGame'] = scoreThatGame

            yearsData.append(data)
        
        return yearsData

    @staticmethod
    def fixUpInningsPitched(ip):
        if (ip[-2:] == '.1'):
            return float(ip.replace('.1', '.333'))
        elif (ip[-2:] == '.2'):
            return float(ip.replace('.2', '.667'))
        else:
            return float(ip)


inputFile = open('listOfNames.txt', 'r')
fan_duel_players = []
for line in inputFile:
    fan_duel_players.append(Player.Player(line, 'b', '1', '1', '1000', '3.2538', 0.0))

f = open('jsonFile.json', 'w')

for player in fan_duel_players:
    print 'trying for: ', player.getName()
    try:
        playerData = {}
        playerData['p'] = PlayerJsonBuilder.getPitcherJson(player)
        playerData['b'] = PlayerJsonBuilder.getBatterJson(player)
        #dataDump[player.getName()] = playerData 
        json_data = json.dumps(playerData)
        f.write('\"'+player.getName() + '\" : ' + json_data + '\n')
        print 'wrote for: ', player.getName()
    except Exception, e:
        print e       
