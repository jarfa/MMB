from Evaluator.EvaluatorBasic import EvaluatorBasic
from Scraper.FanDuelScraper import FanDuelScraper

__author__ = 'Mike'

fan_duel_game_url = "https://www.fanduel.com/e/Game/12662"

scraper = FanDuelScraper(fan_duel_game_url)
fan_duel_players = scraper.get_fan_duel_players()

evaluator_basic = EvaluatorBasic()

for player in fan_duel_players:
    player.print_player()
    print str(evaluator_basic.getPlayerValue(player))