# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

# TODO This is your code!
sys.path.insert(1, '../group24')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *

#for i in range(0, 100):
g = Game.fromfile('map.txt')
g.add_monster(SelfPreservingMonster("monster", # name
                                        "M",       # avatar
                                        3, 9,      # position
                                        1          # detection range
                                        ))

    # 89% win rate (100 attempts)
qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists],
                        [8.564012007264198, -3.0569255103512067, 0.06834293304145697, -6.878067177939179, 7.26429976929269])

g.add_character(qlCharacter("me", # name
                               "C",  # avatar
                               0, 0,  # position
                               qLearner,
                               False,1,1))

    # Run!
g.go()
    #print(g.world.scores["me"])