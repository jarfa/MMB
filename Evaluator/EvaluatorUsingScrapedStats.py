__author__ = 'Kevin'

# anchor extraction from html document
from lxml import html
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
				break;
		return currentScore

e = EvaluatorUsingScrapedStats(5)
score = e.getPlayerValue('whocares')
print 'Final score: ', score