import Evaluator


class EvaluatorBasic(Evaluator.Evaluator):
	def getPlayerValue(self, player):
		return player.getFPPG()