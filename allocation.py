
from openopt import *

def make_list(players, budget=35000):
    """
    players is a list of dicts, each with keys:
    id, name, cost, value, 
    P, C, 1B, 2B, 3B, SS, OF
    - player_id is {3 letter team code}_{jersey number}
    - player positions variables are either 1 or 0
    """
    constraints = lambda values: ( #I suspect it won't be able to handle ==
                            values['cost'] <= budget,
                            values['P'] <= 1
                            values['C'] <= 1
                            values['1B'] <= 1
                            values['2B'] <= 1
                            values['3B'] <= 1
                            values['SS'] <= 1
                            values['OF'] <= 3
                            )
    objective = "value"
    p = KSP(objective, players, constraints = constraints, name = 'list_opt')
    r = p.solve('interalg', plot=1, iprint = 1) #could also solve with 'glpk'
    # see r.solutions, r.solutions.coords, r.solutions.values



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
            
        if roster.is_full()
                break

    #testing
    roster.test_invariants(budget)

if __name__ == "__main__":
    simple_list()
