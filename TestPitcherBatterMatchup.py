import EvaluatorUsingScrapedStats
from Player import Player

__author__ = 'Mike'

pitcher = Player("Danny Salazar", "P", "597", "21118", "8800", 12.9, 0)
batter = Player("Miguel Cabrera", "1B", "598", "5118", "5100", 3.5, 0)

print "Pulled Match Ups"

EvaluatorUsingScrapedStats.get_pitcher_batter_matchup(pitcher, batter)

