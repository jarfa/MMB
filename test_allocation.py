from Player import Player
from Roster import Roster
import allocation
import random

import logging


random.seed(5)
P_LIST = [
    Player(
        "p_%s" % i,
        random.choice(["P", "C", "1B", "2B", "3B", "SS", "OF"]),
        str(i),
        "p_%s" % i,
        random.uniform(3e3,5e3),
        random.random() * 100,
        None,
        value = random.random() * 1000
        ) for i in range(1000)
]
# name, position, team_number, fan_duel_id, fan_duel_cost, fan_duel_fppg, injury_suspension_status, baseball_reference_id=None, value=None

def main(logger):
    simple_roster = allocation.simple_list(P_LIST, budget=35000, logger=logger)
    logger.info("Simple roster: %s", simple_roster)
    logger.info("Simple roster value: %s " , simple_roster.get_value())

    genetic_roster = allocation.genetic_list(P_LIST, budget = 35000, epochs=10, 
        num_children = 5, num_survivors = 3, num_remove = 2, rseed=10, logger=logger)
    logger.info("Genetic roster: %s", genetic_roster)
    logger.info("Genetic roster value: %s " , genetic_roster.get_value())


if __name__ == '__main__':
    # logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
    logger = logging.getLogger(__name__)
    logger.info('Started logging')
    main(logger)
