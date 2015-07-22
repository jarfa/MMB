from EvaluatorUsingScrapedStats import EvaluatorUsingScrapedStats
import FanDuelScraper
import allocation
import logging

__author__ = 'Mike'

# fan_duel_game_url = "https://www.fanduel.com/e/Game/12664"
fan_duel_game_url = ""

# all_players = PlayersLoader.get_all_players()
fan_duel_players = FanDuelScraper.get_fan_duel_players(fan_duel_game_url)

# merge_player(all_players, fan_duel_players)

evaluator = EvaluatorUsingScrapedStats(5)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.info('Started logging')

doNotMakeMeHateYou = 0

for player in fan_duel_players.values():
    #player.print_player()
    doNotMakeMeHateYou += 1
    if(doNotMakeMeHateYou < 20):
    	score = evaluator.getPlayerValue(player)
    	player.setValue(score)
    	print 'player: ', player.getName(), ' got a score of: ', str(player.getValue())
    else:
    	player.setValue(0)

print'\n------ time to see who to use -------\n'
genetic_roster = allocation.genetic_list(fan_duel_players, budget = 35000, epochs=10, 
    num_children = 5, num_survivors = 3, num_remove = 2, rseed=10, logger=logger)
logger.info("Genetic roster: %s", genetic_roster)
logger.info("Genetic roster value: %s " , genetic_roster.get_value())


def merge_player(all_players, fan_duel_players):
    for fan_duel_player in fan_duel_players.values():
        player = all_players[fan_duel_player.getMMBID()]
        player.set_fan_duel_values(fan_duel_player)

