



def simple_list(player_list, budget = 35000):
    """
    player_list is a list of Player objects
    sort players by value/cost
    for each player, starting by the 'best'
        take the player IF we have a slot for it and it's under budget

    """
    roster = Roster()
    player_list.sort(key=lambda p: p.value/p.cost, reverse=True)
    
    for p in player_list:
        if roster.allocated[p.position] < roster.limits[p.position] \
        and (budget - p.cost) > 0:
            roster.add(p)
            budget -= p.cost
        else: # look at the next best player
            continue

    #testing
    roster.test_invariants(budget)

if __name__ == "__main__":
    simple_list()
