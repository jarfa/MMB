import TeamNumberToNameMapping

__author__ = 'MMB'
class Player(object):

    def __init__(self, name, position, team_number, fan_duel_id, fan_duel_cost, fan_duel_fppg, injury_suspension_status, baseball_reference_id=None, value=None):
        self.mmb_id = name + "." + str(team_number)
        self.name = name
        self.position = position
        self.team_number = str(team_number)
        self.fan_duel_id = fan_duel_id
        self.fan_duel_cost = float(fan_duel_cost)
        self.fan_duel_fppg = float(fan_duel_fppg)
        self.injury_suspension_status = injury_suspension_status
        self.baseball_reference_id = baseball_reference_id
        self.value = value

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.name, self.mmb_id, self.fan_duel_cost, self.value)

    def print_player(self):
        print "MMB ID: " + self.mmb_id
        print "Name: " + self.name
        print "Position: " + self.position
        print "Team Number: " + self.team_number
        print "Fan Duel Id: " + self.fan_duel_id
        print "Fan Duel Cost: " + str(self.fan_duel_cost)
        print "Fan Duel FPPG: " + str(self.fan_duel_fppg)
        print "Value: " + str(self.value)
        print "Injury/Suspension Status: " + str(self.injury_suspension_status)
        print ""

    def getFPPG(self):
        return self.fan_duel_fppg

    def getName(self):
        return self.name

    def getTeamNumber(self):
        return self.team_number

    def getTeamName(self):
        return TeamNumberToNameMapping.get_team_name(self.team_number)

    def getFirstName(self):
        return self.name.split(" ", 1)[0]

    def getLastName(self):
        return self.name.split(" ", 1)[1]

    def getInjurySuspensionStatus(self):
        return self.injury_suspension_status

    def getBaseballReferenceId(self):
        return self.baseball_reference_id

    def setBaseballReferenceId(self, baseball_reference_id):
        self.baseball_reference_id = baseball_reference_id

    def getPosition(self):
        return self.position




