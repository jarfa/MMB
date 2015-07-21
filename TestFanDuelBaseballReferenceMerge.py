from EvaluatorUsingScrapedStats import EvaluatorUsingScrapedStats
from Player import Player

__author__ = 'Mike'

player = Player("Danny Salazar", "P", "597", "21118", "8800", 12.9, 0)

assert player.getName() == "Danny Salazar"
assert player.getPosition() == "P"
assert player.getTeamNumber() == "597"
assert player.getTeamName() == "Indians"
assert player.getInjurySuspensionStatus() == 0
assert player.getFanDuelCost() == 8800

print player.getBaseballReferenceId()
print player.get_player_page_url()
assert player.getBaseballReferenceId()
assert player.get_player_page_url()

