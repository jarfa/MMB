# http://openopt.org/KSP
# http://trac.openopt.org/openopt/browser/PythonPackages/OpenOpt/openopt/examples/ksp_2.py

from openopt import *

def make_list(players, budget=35000):
    """
    players is a list of dicts, each with keys:
    id, name, cost, value, 
    P, C, 1B, 2B, 3B, SS, OF
    - player_id is {3 letter team code}_{jersey number}
    - player positions variables are either 1 or 0
    """
    constraints = lambda values: ( #I suspect it won't be able to handle ==
                            values['cost'] <= budget,
                            values['P'] <= 1
                            values['C'] <= 1
                            values['1B'] <= 1
                            values['2B'] <= 1
                            values['3B'] <= 1
                            values['SS'] <= 1
                            values['OF'] <= 3
                            )
    objective = "value"
    p = KSP(objective, players, constraints = constraints, name = 'list_opt')
    r = p.solve('interalg', plot=1, iprint = 1) #could also solve with 'glpk'
    # see r.solutions, r.solutions.coords, r.solutions.values

if __name__ == "__main__":
    make_list() #fill in stuff
