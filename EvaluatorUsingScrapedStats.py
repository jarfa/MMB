__author__ = 'Kevin'

# anchor extraction from html document
from lxml import html
import requests
import Evaluator
import Player


class EvaluatorUsingScrapedStats(Evaluator.Evaluator):

    def __init__(self, cutoff=5):
        self.cutoff = cutoff

    @staticmethod
    def getBatterUrl(player):
        # sample url -- http://www.baseball-reference.com/players/gl.cgi?id=poseybu01&t=b&year=2015
        return 'http://www.baseball-reference.com/players/gl.cgi?id=' + player.getLastName().lower()[:5] + player.getFirstName().lower()[:2] +'01&t=b&year=2015'

    @staticmethod
    def getPitcherUrl(player):
        return 'http://www.baseball-reference.com/players/gl.cgi?id=' + player.getLastName().lower()[:5] + player.getFirstName().lower()[:2] +'01&t=p&year=2015'

    def getPlayerValue(self, player):
        score = 0
        if(player.getPosition() == 'p'):
            score += EvaluatorUsingScrapedStats.getPitcherScore(self.cutoff)
            #TODO::if the pitcher will be batting add their batter score
        else:
            score += EvaluatorUsingScrapedStats.getBatterScore(self.cutoff)

        return score

    @staticmethod
    def getBatterScore(cutoff):
        page = requests.get(EvaluatorUsingScrapedStats.getBatterUrl(player))
        tree = html.fromstring(page.text)
        stuff = tree.xpath('//tr[contains(@id,"batting_gamelogs")]')
        currentScore = 0
        iteration=0
        for i in reversed(stuff):
            hits = int(i.findtext('.//td[13]'))
            twoB = int(i.findtext('.//td[14]'))
            threeB = int(i.findtext('.//td[15]'))
            hr = int(i.findtext('.//td[16]'))
            rbi = int(i.findtext('.//td[17]'))
            runs = int(i.findtext('.//td[12]'))
            bb = int(i.findtext('.//td[18]'))
            sb = int(i.findtext('.//td[26]'))
            hbp = int(i.findtext('.//td[21]'))
            atBats = int(i.findtext('.//td[11]'))
            outs = atBats - hits
            scoreThatGame = hits + 2*twoB + 3*threeB + 4*hr + rbi + runs + bb + 2*sb + hbp - outs/float(4)
            print 'hits: ', hits, ', 2b: ', twoB, ', 3b: ', threeB, ', hrs: ', hr, ', rbi: ', rbi, ', runs: ', runs, ', bb: ', bb, ', sb: ', sb, ', hbp ', hbp, ', outs ', outs, ', score: ', scoreThatGame
            currentScore += scoreThatGame
            
            iteration += 1
            if(iteration >= cutoff):
                break
        return currentScore / float(iteration)

    @staticmethod
    def getPitcherScore(cutoff):
        page = requests.get(EvaluatorUsingScrapedStats.getPitcherUrl(player))
        tree = html.fromstring(page.text)
        stuff = tree.xpath('//tr[contains(@id,"pitching_gamelogs")]')
        currentScore = 0
        iteration=0
        for i in reversed(stuff):
            result = i.findtext('.//td[8]')
            win = (result[:1] == 'W')

            ip = EvaluatorUsingScrapedStats.fixUpInningsPitched(i.findtext('.//td[12]/span').strip()) #they do x.1 and x.2 for outs and we need x.33 and x.66
            so = int(i.findtext('.//td[17]'))
            er = int(i.findtext('.//td[15]'))

            scoreThatGame = 0
            if(win):
                scoreThatGame = 4
            scoreThatGame += ip + so - er
            print 'win: ', win, ', ip: ', ip, ', so: ', so, ', er: ', er, 'score: ', scoreThatGame
            currentScore += scoreThatGame
            
            iteration += 1
            if(iteration >= cutoff):
                break
        return currentScore / float(iteration)

    @staticmethod
    def fixUpInningsPitched(ip):
        if (ip[-2:] == '.1'):
            return float(ip.replace('.1', '.333'))
        elif (ip[-2:] == '.2'):
            return float(ip.replace('.2', '.667'))
        else:
            return float(ip)

    def get_pitcher_batter_matchup(self, pitcher, batter):
        pitcher_batter_url = "http://www.baseball-reference.com/play-index/batter_vs_pitcher.cgi?batter=" \
                             + batter.getBaseballReferenceId() + "&pitcher=" + pitcher.getBaseballReferenceId()




e = EvaluatorUsingScrapedStats(5)
#Player(name, position, team_number, fan_duel_id, fan_duel_cost, fan_duel_fppg, value)
player = Player.Player('Buster Posey', 'b', '1', '1', '1000', '3.2538', 0.0)
#player = Player.Player('Dan Haren', 'p', '1', '1', '1000', '3.2538', 0.0)
score = e.getPlayerValue(player)
print 'Final score: ', score