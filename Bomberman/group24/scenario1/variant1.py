# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game

sys.path.insert(1, '../group24')

# Uncomment this if you want the empty test character
#from testcharacter import TestCharacter

# Uncomment this if you want the interactive character
from interactivecharacter import InteractiveCharacter
from ascharacter import AsCharacter
sys.path.insert(1, '../group24')
from qlcharacter import qCharacter
from qlearning import QLearner
from qlhelpers import *

# Create the game
g = Game.fromfile('map.txt')

#c = OurCharacter( "me", "C", 0, 0, g.world)
#c.makepath(g.world)

qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists],
                    [9.644738825307972, 0.0, -0.7636358419388961, -5.971568757785089, 5.7744223269435375])

# TODO Add your character
#g.add_character(AsCharacter("me",
#                             "C",
#                             0,0,
#                             g.world
#))

g.add_character(qCharacter("me", # name
                           "C",  # avatar
                           0, 0,  # position
                           qLearner,
                           False,1,1))

# Uncomment this if you want the test character
# g.add_character(TestCharacter("me", # name
#                               "C",  # avatar
#                               0, 0  # position
# ))

# Uncomment this if you want the interactive character
#g.add_character(InteractiveCharacter("me", # name
 #                                    "C",  # avatar
  #                                   0, 0  # position
#))

# Run!

# Use this if you want to press ENTER to continue at each step
#g.go(0)

# Use this if you want to proceed automatically
g.go(1)
