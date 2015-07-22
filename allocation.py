import logging
import random
from Roster import Roster

def roster_log(logger, roster, budget, remaining):
    logger.info("Built roster %s with remaining budget %d/%d", 
        roster, remaining, budget)

def simple_list(player_list, budget = 35000, logger=None):
    """
    player_list is a list of Player objects
    sort players by value/cost
    for each player, starting by the 'best'
        take the player IF we have a slot for it and it's under budget
    """
    remaining_budget = budget
    roster = Roster()
    min_cost = sorted(p.getFanDuelCost() for p in player_list)[9]
    player_list.sort(key=lambda p: p.getFPPG(), reverse=True)
    
    for p in player_list:
        if roster.allocated[p.position] < roster.limits[p.position] and \
        remaining_budget - p.fan_duel_cost >= (9 - roster.length() - 1)* min_cost:
            roster.add(p)
            remaining_budget -= p.fan_duel_cost
            logger.debug("Currently have %d players: %s", roster.length(), roster)
            logger.debug("Budget: %d/%d", remaining_budget, budget)
        elif logger.getEffectiveLevel() <= logging.DEBUG: 
            if p.fan_duel_cost > remaining_budget:
                reason_string = "player cost (%d) was over remaining budget (%d/%d)" % (
                    p.fan_duel_cost, remaining_budget, budget)
            else:
                reason_string = "slot for position %s already has %d members" % (
                    p.position, roster.allocated[p.position])

            logger.debug(("Skipped %s because " % p.name) + reason_string)
            
        if roster.is_full():
                break

    roster.test_invariants(budget)
    if logger.getEffectiveLevel() <= logging.DEBUG: 
        roster_log(logger, roster, budget, remaining_budget)
    return roster

def mutate_roster(roster, player_list, budget, num_remove=2, logger=None):
    #take away num_remove of the current roster, re-build using other players
    remove_list = random.sample(roster.player_list, num_remove)
    new_list = list(set(player_list) - set(remove_list))
    roster.test_invariants(budget)
    return simple_list(new_list, budget, logger=logger)

def genetic_list(player_list, budget = 35000, epochs=10, num_children = 5, 
    num_survivors = 3, num_remove = 2, rseed=10, logger=None):
    random.seed(rseed)
    #initialize simple_list
    survivors = [simple_list(player_list, budget, logger=logger)] #1-length list for the first iteration
    #mutating means remove 1 (or 2?) players that are currently in the roster from player_list, try again
    for e in xrange(epochs):
        children = list(survivors)
        for s in survivors:
            for _ in xrange(num_children):
                children.append(mutate_roster(s, player_list, budget, num_remove, logger))
        logger.info("%d children at epoch %d" % (len(children), e))
        values = [c.get_value() for c in children]
        logger.info("Best: %d, Worst: %d", max(values), min(values))
        survivors = sorted(children, key=lambda c: c.get_value(), reverse=True)[:num_survivors]
        logger.info("Survivor values: (%s)", ",".join(str(s.get_value()) for s in survivors))

    champion = max(survivors, key=lambda c: c.get_value())
    roster_log(logger, champion, budget, budget - champion.get_cost())
    return champion

if __name__ == "__main__":
    pass
