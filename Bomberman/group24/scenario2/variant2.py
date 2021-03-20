# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.stupid_monster import StupidMonster

# TODO This is your code!
sys.path.insert(1, '../group24')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *

# Create the game
g = Game.fromfile('map.txt')
g.add_monster(StupidMonster("monster", # name
                            "M",       # avatar
                            3, 9       # position
                            ))

# Current status: 99% success totally trained
qLearner = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [163.74500850965978, -74.81375861611413, -3.710392437626575, 26.26781955724994, 71.22790728981906, 42.2166434790756, 3.47072116678088])

g.add_character(qlCharacter("me", # name
                           "C",  # avatar
                           0, 0,  # position
                           qLearner,
                           False,1,1))

# Run!
g.go()
