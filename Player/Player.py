__author__ = 'MMB'
class Player(object):

    def __init__(self, name, position, team_number, fan_duel_id, fan_duel_cost, fan_duel_fppg):
        self.mmb_id = name + "." + team_number
        self.name = name
        self.position = position
        self.team_number = team_number
        self.fan_duel_id = fan_duel_id
        self.fan_duel_cost = float(fan_duel_cost)
        self.fan_duel_fppg = float(fan_duel_fppg)


    def print_player(self):
        print "MMB ID: " + self.mmb_id
        print "Name: " + self.name
        print "Position: " + self.position
        print "Team Number: " + self.team_number
        print "Fan Duel Id: " + self.fan_duel_id
        print "Fan Duel Cost: " + str(self.fan_duel_cost)
        print "Fan Duel FPPG: " + str(self.fan_duel_fppg)
        print ""



