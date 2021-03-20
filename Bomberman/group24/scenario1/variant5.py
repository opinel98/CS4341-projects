# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster

# TODO This is your code!
sys.path.insert(1, '../group24')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *

qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists, f_within_two_of_monster],
                    [6.816656292974258, -2.214658827136486, -0.5886164957366603, -8.324788954040265, 4.402454683798063, 0])

# Create the game
wins = 0
#for i in range(0, 100):
g = Game.fromfile('map.txt')
g.add_monster(StupidMonster("monster", # name
                                "S",       # avatar
                                3, 5,      # position
                                ))
g.add_monster(SelfPreservingMonster("monster", # name
                                        "A",       # avatar
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

    #if g.world.scores["me"] > 0:
    #    wins += 1
    #print("{}, {:.2f}%".format(g.world.scores["me"], wins/(i+1)*100))
