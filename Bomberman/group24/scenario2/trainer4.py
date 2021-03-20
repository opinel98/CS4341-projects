# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

sys.path.insert(1, '../group26')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *

#Current status: 88% win rate, completely trained
qLearner = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [159.33304471198795, -78.09792999957172, -18.750314892480493, 5.0167239427069035, 121.1905955320059, 124.59454062803833, 3.716190063440644])

won = 0
count = 0

for i in range(0, 100):
    print("Running iteration #"+str(i))
    # Create the game
    g = Game.fromfile('map.txt')

    g.add_monster(SelfPreservingMonster("monster",  # name
                                        "M",  # avatar
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
        won += 1

print("Won " + str(won/count) + " percent of the time")