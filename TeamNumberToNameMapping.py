__author__ = 'Mike'

class TeamNumberToNameMapping:
    team_number_to_name_map = {'591': 'Orioles',
                               '592': 'Red Sox',
                               '593': 'Yankees',
                               '594': 'Rays',
                               '595': 'Blue Jays',
                               '596': 'White Sox',
                               '597': 'Indians',
                               '598': 'Tigers',
                               '599': 'Royals',
                               '600': 'Twins',
                               '601': 'Angels',
                               '602': 'Athletics',
                               '603': 'Mariners',
                               '604': 'Rangers',
                               '605': 'Braves',
                               '606': 'Marlins',
                               '607': 'Mets',
                               '608': 'Phillies',
                               '609': 'Nationals',
                               '610': 'Cubs',
                               '611': 'Reds',
                               '612': 'Astros',
                               '613': 'Brewers',
                               '614': 'Pirates',
                               '615': 'Cardinals',
                               '616': 'Diamondbacks',
                               '617': 'Rockies',
                               '618': 'Dodgers',
                               '619': 'Padres',
                               '620': 'Giants'
    }

    @staticmethod
    def get_team_name(team_number):
        return TeamNumberToNameMapping.team_number_to_name_map[team_number]