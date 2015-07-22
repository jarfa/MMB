__author__ = 'Mike'

class Matchup:
    def __init__(self, home_team, away_team, home_pitcher, away_pitcher):
        self.home_team = home_team
        self.away_team = away_team
        self.home_pitcher = home_pitcher
        self.away_pitcher = away_pitcher

    def __repr__(self):
        return "Home: %s, Away: %s, HP: %s, AP: %s" % (self.home_team, self.away_team, self.home_pitcher, self.away_pitcher)