# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

# TODO This is your code!
# Import necessary stuff
import random
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

# TODO This is your code!
sys.path.insert(1, '../group24')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *

# Create the game
qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists, f_within_two_of_monster],
                    [6.677040814273156, -2.8712762824080875, 0.0007472148776999527, -0.9223685778177153, 4.6431419153438666e-05, -0.05143683159538506]) # About 78-80%

# Approximately 64%:
wins = 0
#for i in range(0, 1000):
g = Game.fromfile('map.txt')
g.add_monster(SelfPreservingMonster("monster", # name
                                        "M",       # avatar
                                        3, 13,     # position
                                        2          # detection range
                                        ))

g.add_character(qlCharacter("me", # name
                               "C",  # avatar
                               0, 0,  # position
                               qLearner,
                               False,1,1))

    # Run!
g.go()

#    if g.world.scores["me"] > 0:
#        wins += 1
#    print("{}, {:.2f}%".format(g.world.scores["me"], wins/(i+1)*100))