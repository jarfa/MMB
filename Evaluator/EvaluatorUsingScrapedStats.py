__author__ = 'Kevin'

# anchor extraction from html document
import html
import requests
import Evaluator

class EvaluatorUsingScrapedStats(Evaluator.Evaluator):

    def __init__(self, cutoff):
        self.cutoff = cutoff
        print self.cutoff

    @staticmethod
    def getUrlToPull(player):
        return 'http://www.baseball-reference.com/players/gl.cgi?id=poseybu01&t=b&year=2015'

    def getPlayerValue(self, player):
        print self.cutoff
        page = requests.get(EvaluatorUsingScrapedStats.getUrlToPull(player))
        tree = html.fromstring(page.text)
        stuff = tree.xpath('//tr[contains(@id,"batting_gamelogs")]')
        currentScore = 0
        iteration=0
        for i in reversed(stuff):
            hits = i.findtext('.//td[13]')
            hr = i.findtext('.//td[16]')
            print 'hits: ', hits, ', hrs: ', hr
            currentScore += int(hits)
            currentScore += (3* int(hr))
            iteration += 1
            if(iteration >= self.cutoff):
                break
        return currentScore

    def get_pitcher_batter_matchup(self, pitcher, batter):
        pitcher_batter_url = "http://www.baseball-reference.com/play-index/batter_vs_pitcher.cgi?batter=" \
                             + self.get_player_id(pitcher) + "&pitcher=" + self.get_player_id(batter)

    def get_player_id(self, player):
        last_name_substr = player.getLastName()[:5]
        first_name_substr = player.getFirstName()[:2]
        name_iteration_number = "01"

        return last_name_substr + first_name_substr + name_iteration_number

    def get_player_page_url(self, player):
        player_id_url = "http://www.baseball-reference.com/players/j/" + self.get_player_id(player) + ".shtml"

    def get_team(self, player):
        self.get_player_page_url(player)
        player_page = requests.get(EvaluatorUsingScrapedStats.getUrlToPull(self.get_player_page_url(player)))
        tree = html.fromstring(player_page.text)
        organization = tree.xpath("//span[contains(@itemprop, 'organization'])")
        print organization

        teams_years_split = organization.split(" ", 1)
        teams = teams_years_split[0]
        years = teams_years_split[1]

        last_team = teams.split("/")[-1]
        last_year = years.split("-")[-1]

        if(last_year == "2015" and last_team ==


# e = EvaluatorUsingScrapedStats(5)
# score = e.getPlayerValue('whocares')
# print 'Final score: ', score