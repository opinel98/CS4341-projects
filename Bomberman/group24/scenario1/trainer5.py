# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster

sys.path.insert(1, '../group24')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *

qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists, f_bomb_to_wall, f_bomb_to_edge, f_char_between_monster_and_bomb, f_char_in_corner, f_char_to_edge_when_monsters])


for i in range(0, 1000):
    print("Running iteration #"+str(i))
    # Create the game
    g = Game.fromfile('map.txt')

    g.add_monster(StupidMonster("monster",  # name
                                "S",  # avatar
                                3, 5,  # position
                                ))
    g.add_monster(SelfPreservingMonster("monster",  # name
                                        "A",  # avatar
                                        3, 13,  # position
                                        2  # detection range
                                        ))

    g.add_character(qlCharacter("me", # name
                               "C",  # avatar
                               0, 0,  # position
                               qLearner,
                               True,
                               i,
                               1000))
    # Run!
    g.go()
    print(qLearner.weights)
    print(g.world.scores["me"])