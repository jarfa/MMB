import Evaluator
from Player.Player import Player

class EvaluatorBasic(Evaluator.Evaluator):
	def getPlayerValue(self, player):
		return player.getFPPG()
		
e = EvaluatorBasic()
#Player(name, position, team_number, fan_duel_id, fan_duel_cost, fan_duel_fppg)
player = Player('test name', 'p', '1', '1', '1000', '3.2538')
score = e.getPlayerValue(player)
print 'Final score: ', score