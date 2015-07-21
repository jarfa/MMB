import EvaluatorUsingScrapedStats

__author__ = 'Mike'

matchups = EvaluatorUsingScrapedStats.getMatchups()

print "Pulled Match Ups"

print len(matchups)
# assert len(fan_duel_players) > 100
for matchup in matchups:
    print matchup
    if(player.getName() == "Danny Salazar"):
        assert player.getPosition() == "P"
        print player.getTeamNumber()
        assert player.getTeamNumber() == "597"
        assert player.getTeamName() == "Indians"
        assert player.getInjurySuspensionStatus() == 0
        assert player.getFanDuelCost() == 8800

        print "Player Successfully from FanDuel"
