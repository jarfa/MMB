from EvaluatorBasic import EvaluatorBasic
import FanDuelScraper
import allocation
import logging

__author__ = 'Mike'

fan_duel_game_url = "https://www.fanduel.com/e/Game/12674"

fan_duel_players = FanDuelScraper.get_fan_duel_players(fan_duel_game_url)

evaluator = EvaluatorBasic()

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.info('Started logging')

for player in fan_duel_players:
 	score = evaluator.getPlayerValue(player)
 	print 'player: ', player.getName(), ' got a score of: ', score
   	player.setValue(score)

print'\n------ time to see who to use -------\n'
simple_roster = allocation.simple_list(fan_duel_players, budget=35000, logger=logger)
logger.info("Simple roster: %s", simple_roster)
logger.info("Simple roster value: %s " , simple_roster.get_value())


genetic_roster = allocation.genetic_list(fan_duel_players, budget = 35000, epochs=20, 
    num_children = 10, num_survivors = 4, num_remove = 2, rseed=10, logger=logger)
logger.info("Genetic roster: %s", genetic_roster)
logger.info("Genetic roster value: %s " , genetic_roster.get_value())
