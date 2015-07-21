import Player

__author__ = 'Mike'

player = Player.Player("Danny Salazar", "P", "597", "21118", "8800", 12.9, 0)

assert(player.getName() == "Danny Salazar")
assert player.getPosition() == "P"
assert player.getTeamNumber() == "597"
assert player.getTeamName() == "Indians"
assert player.getInjurySuspensionStatus() == 0
assert player.getFanDuelCost() == 8800

print "Player Successfully Created"
