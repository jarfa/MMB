__author__ = 'Mike'

class Roster:
    def __init__(self, limits = {
        'P':1, 'C':1, '1B':1, '2B': 1, '3B': 1, 'SS': 1, 'OF': 3
        }):
        self.limits = limits
        self.allocated = dict((k,0) for k  in limits.keys())
        self.player_list = []

    def add(self, player):
        if self.allocated[player.position] + 1 > self.limits[player.position]:
            raise Exception(
                "Can't add, already have enough players at position %s (limit %d)" %
                (player.position, self.limits[player.position]))
        self.allocated[player.position] += 1
        self.player_list.append(player)

    def __repr__(self):
        for p in player_list:
            print "%s: %s" % (player.name, player.position)