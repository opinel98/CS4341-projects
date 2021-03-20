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

#Current Status: about 85%, purely trained
qLearner = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [169.5792884684401, -89.43359914000227, -9.055797124970724, 5.3165976373538, 100.30312257082886, 71.41381770528874, 4.911815807943525])

# Create the game

g = Game.fromfile('map.txt')
g.add_monster(SelfPreservingMonster("monster", # name
                                    "M",       # avatar
                                    3, 9,      # position
                                    1          # detection range
                                    ))

g.add_character(qlCharacter("me", # name
                           "C",  # avatar
                           0, 0,  # position
                           qLearner,
                           False,1,1))

# Run!
g.go()
