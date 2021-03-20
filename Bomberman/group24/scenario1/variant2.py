# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.stupid_monster import StupidMonster
from ascharacter import AsCharacter

# TODO This is your code!
sys.path.insert(1, '../group24')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *

# Current status: 99% in 100 attempts
qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists],
                    [8.458119902186587, -3.0418798099256046, -0.31907802641410155, -3.770071502872679, 7.126050209167285])

# Create the game
#for i in range(0, 100):
g = Game.fromfile('map.txt')
g.add_monster(StupidMonster("monster", # name
                                "M",       # avatar
                                3, 9       # position
                                ))

g.add_character(qlCharacter("me", # name
                               "C",  # avatar
                               0, 0,  # position
                               qLearner,
                               False,1,1))

# Run!
g.go()
    #print(g.world.scores["me"])
