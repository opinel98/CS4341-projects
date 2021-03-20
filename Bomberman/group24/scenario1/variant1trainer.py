# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game

sys.path.insert(1, '../group24')
from q_character import qCharacter
from q_learning import QLearner
from q_functions import *

qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists])

for i in range(0, 100):
    print("Running iteration #"+str(i))
    # Create the game
    g = Game.fromfile('map.txt', display=False)

    g.add_character(qCharacter("me", # name
                               "C",  # avatar
                               0, 0,  # position
                               qLearner,
                               True,
                               i,
                               1000))
    # Run!
    g.go()
    print(g.world.scores["me"])
    print(qLearner.weights)