



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
        if roster.allocated[p.position] < roster.limits[p.position] \
        and remaining_budget >= p.cost:
            roster.add(p)
            remaining_budget -= p.cost
        else: # look at the next best player
            if p.cost > remaining_budget:
                reason_string = "player (cost %d) was over remaining_budget (%d)" % (
                    p.cost, remaining_budget)
            else:
                reason_string = "slot for %s already has %d members" % (
                    p.position, roster.allocated[p.position])

            print "Skipped %s because " + 
            continue

    #testing
    roster.test_invariants(budget)

if __name__ == "__main__":
    simple_list()
