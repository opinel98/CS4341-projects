# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster

sys.path.insert(1, '../group26')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *

qLearner = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [164.12592154785062, -72.35351066390663, -18.986104409901127, 8.473394337312714, 218.7488044723275, 224.56932851491754, 1.7431601829087855])

count = 0
wins = 0

for i in range(0, 100):
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
                               False,
                               i,
                               1000))
    # Run!
    g.go()
    print(qLearner.weights)
    print(g.world.scores["me"])
    count += 1
    if g.world.scores["me"] > 0:
        wins += 1

print("Won " + str(wins/count) + " percent of the time")