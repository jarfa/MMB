

import random
from Roster import Roster

# from openopt import *
# def knapsack_list(players, budget=35000):
#     """
#     players is a list of dicts, each with keys:
#     id, name, cost, value, 
#     P, C, 1B, 2B, 3B, SS, OF
#     - player_id is {3 letter team code}_{jersey number}
#     - player positions variables are either 1 or 0
#     """
#     constraints = lambda values: ( #I suspect it won't be able to handle ==
#                             values['cost'] <= budget,
#                             values['P'] <= 1,
#                             values['C'] <= 1,
#                             values['1B'] <= 1,
#                             values['2B'] <= 1,
#                             values['3B'] <= 1,
#                             values['SS'] <= 1,
#                             values['OF'] <= 3,
#                             )
#     objective = "value"
#     p = KSP(objective, players, constraints = constraints, name = 'list_opt')
#     r = p.solve('interalg', plot=1, iprint = 1) #could also solve with 'glpk'
#     # see r.solutions, r.solutions.coords, r.solutions.values

def simple_list(player_list, budget = 35000):
    """
    player_list is a list of Player objects
    sort players by value/cost
    for each player, starting by the 'best'
        take the player IF we have a slot for it and it's under budget
    """
    remaining_budget = budget
    roster = Roster()
    player_list.sort(key=lambda p: p.value/p.cost, reverse=True)
    
    for p in player_list:
        if roster.allocated[p.position] < roster.limits[p.position] and \
                remaining_budget >= p.cost:
            roster.add(p)
            remaining_budget -= p.cost
        else: # look at the next best player
            if p.cost > remaining_budget:
                reason_string = "player cost (%d) was over remaining budget (%d/%d)" % (
                    p.cost, remaining_budget, budget)
            else:
                reason_string = "slot for position %s already has %d members" % (
                    p.position, roster.allocated[p.position])

            print ("Skipped %s because " % p.name) + reason_string
            
        if roster.is_full():
                break

    #testing
    roster.test_invariants(budget)

    return roster

def mutate_roster(roster, player_list, budget, num_remove=2):
    remove_list = random.sample(roster.player_list, num_remove)
    new_list = list(set(player_list) - set(remove_list))
    return simple_list(new_list, budget)

def genetic_list(player_list, budget = 35000, epochs=10, num_children = 5, 
    num_survivors = 3, num_remove = 2, seed=10):
    random.seed(seed)
    #initialize simple_list
    survivors = [simple_list(player_list, budget)] #1-length list for the first iteration
    #mutating means remove 1 (or 2?) player that's currently in the roster from player_list, try again
    for e in xrange(epochs):
        children = []
        for s in survivors:
            children += [mutate_roster(s, player_list, budget, num_remove) 
                        for _ in xrange(num_children)]
        survivors = sorted(children, lambda x: x.get_value(), 
            reverse=True)[:num_survivors]

    best = max(survivors, key=lambda x: x.get_value())
    return best

if __name__ == "__main__":
    pass
