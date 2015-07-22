import TeamNumberToNameMapping
from lxml import html
import requests
import re

__author__ = 'MMB'
class Player(object):

    def __init__(self, name, position, team_number, fan_duel_id, fan_duel_cost, fan_duel_fppg, injury_suspension_status, baseball_reference_id="", value=None):
        name_mod = re.sub("[^A-Za-z0-9 ]","",name)
        # if name != name_mod:
        #     print name
        #     print name_mod
        #     print ""

        self.mmb_id = name_mod + "." + str(team_number)
        self.name = name_mod
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

    def getMMBID(self):
        return self.mmb_id

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

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
        if self.baseball_reference_id == "":
            self.find_baseball_reference_player_id()
        return self.baseball_reference_id

    def setBaseballReferenceId(self, baseball_reference_id):
        self.baseball_reference_id = baseball_reference_id

    def getPosition(self):
        return self.position

    def getFanDuelCost(self):
        return self.fan_duel_cost

    def get_player_page_url(self):
        return Player.construct_player_page_url(self.getBaseballReferenceId())

    def find_baseball_reference_player_id(self):
        last_name_substr = self.getLastName()[:5].lower()
        first_name_substr = self.getFirstName()[:2].lower()
        name_iteration_number = 1

        found_baseball_reference_player_id = False
        while not found_baseball_reference_player_id and name_iteration_number < 10:
            print found_baseball_reference_player_id
            print name_iteration_number

            name_iteration_number_string =  "%02d" % (name_iteration_number,)

            test_player_id = last_name_substr + first_name_substr + name_iteration_number_string
            if self.validate_team(test_player_id):
                self.setBaseballReferenceId(test_player_id)
                found_baseball_reference_player_id = True

            name_iteration_number += 1

    def validate_team(self, test_player_id):
        player_page_url = Player.construct_player_page_url(test_player_id)
        player_page = requests.get(player_page_url)
        tree = html.fromstring(player_page.text)
        organization = tree.xpath("//span[contains(@itemprop, 'organization')]")[0].text_content()

        teams_years_split = organization.split(" ", 1)
        teams = teams_years_split[0]
        years = teams_years_split[1]

        last_team = teams.split("/")[-1]
        last_year = years.split("-")[-1]

        if last_year == "2015" and last_team == self.getTeamName():
            return True

        return False

    def set_fan_duel_values(self, fan_duel_player):
        self.team_number = fan_duel_player.team_number
        self.fan_duel_id = fan_duel_player.fan_duel_id
        self.fan_duel_cost = fan_duel_player.fan_duel_cost
        self.fan_duel_fppg = fan_duel_player.fan_duel_fppg


    @classmethod
    def construct_player_page_url(cls, baseball_reference_id):
        first_character = baseball_reference_id[0]
        return "http://www.baseball-reference.com/players/" + first_character + "/" + baseball_reference_id + ".shtml"



