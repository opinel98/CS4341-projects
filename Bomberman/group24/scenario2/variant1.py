# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game

# TODO This is your code!
sys.path.insert(1, '../group24')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *


# Create the game
g = Game.fromfile('map.txt')

# Current status: 100% success rate, trained
qLearner = QLearner([f_to_exit, f_is_exploded_now, f_bomb_to_wall, f_time_to_explosion], [157.52129963352013, -65.41935486086436, 28.856877994965103, 20.48922401645315])

g.add_character(qlCharacter("me", # name
                           "C",  # avatar
                           0, 0,  # position
                           qLearner,
                           False,1,1))

# Run!
g.go()
print(g.world.scores)
