from EvaluatorBasic import EvaluatorBasic
import FanDuelScraper

__author__ = 'Mike'

fan_duel_game_url = "https://www.fanduel.com/e/Game/12662"

fan_duel_players = FanDuelScraper.get_fan_duel_players(fan_duel_game_url)

evaluator_basic = EvaluatorBasic()

for player in fan_duel_players:
    player.print_player()
    print str(evaluator_basic.getPlayerValue(player))