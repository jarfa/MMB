import Evaluator
from Player.Player import Player

class EvaluatorBasic(Evaluator.Evaluator):
	def getPlayerValue(self, player):
		return player.getFPPG()