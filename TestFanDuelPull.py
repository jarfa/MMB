import FanDuelScraper

__author__ = 'Mike'

fan_duel_game_url = "https://www.fanduel.com/e/Game/12664"

fan_duel_players = FanDuelScraper.get_fan_duel_players(fan_duel_game_url)

print "Pulled Fan Duel Data"

print len(fan_duel_players)
assert len(fan_duel_players) > 100
for player in fan_duel_players:
    if player.getName() == "Danny Salazar":
        assert player.getPosition() == "P"
        print player.getTeamNumber()
        assert player.getTeamNumber() == "597"
        assert player.getTeamName() == "Indians"
        assert player.getInjurySuspensionStatus() == 0
        assert player.getFanDuelCost() == 8800

        print "Player Successfully from FanDuel"
