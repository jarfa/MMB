__author__ = 'Mike'

class Roster:
    def __init__(self, limits={
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
        #sort this?
       return "(" + ",".join("%s: %s" % (p.name, p.position) for p in self.player_list) + ")"

    def length(self):
        return len(self.player_list)

    def is_full(self):
        for p,num in self.allocated.iteritems():
            if num < self.limits[p]:
                return False

        return True

    def get_value(self):
        return sum(p.value for p in self.player_list)

    def get_cost(self):
        return sum(p.fan_duel_cost for p in self.player_list)

    def test_invariants(self, budget=None):
        if budget:
            assert budget >= sum(p.fan_duel_cost for p in self.player_list)

        assert self.length() == sum(self.limits.values())

        for k,v in self.allocated.iteritems():
            if v != self.limits[k]:
                raise Exception("For position %s, %d allocated out of %d" %
                (k, v, self.limits[k]))
