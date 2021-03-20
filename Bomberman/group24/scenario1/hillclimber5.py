# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster
from monsters.stupid_monster import StupidMonster

sys.path.insert(1, '../group24')
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *

from copy import deepcopy
import random
import time


def run(learner, seed):
    random.seed(seed)
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
                               learner,
                               False,
                               0,
                               1000))

    # Run!
    g.go()
    return g.world.scores["me"]


functions = [f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists, f_within_two_of_monster]



qLearner_base = QLearner(functions,
                         [4.461871799497596, -2.214658827136486, -0.5153270948384178, -8.324788954040265, 5.269938302682641, 0])

seeds = [860181728, 35541708273, 6386744544, 41973754893, 10666263840, 11388832667, 41755676819, 94971597375, 80143628391, 17433699535, 99674361376, 56938819189, 73629257677, 88581496873, 69642875155, 44691881728, 40249539589, 62459241947, 95384869582, 57679583426]

base_wins = 0

ALPHA = 0.3

while True:
    random.seed(time.time())
    qLearner_new = QLearner(functions, deepcopy(qLearner_base.weights))
    weight = random.randint(0, len(qLearner_base.weights)-1)
    sign = random.choice([-1, 1])
    qLearner_new.weights[weight] += qLearner_new.weights[weight] * sign * random.random() * ALPHA
    wins = 0
    for seed in seeds:
        if run(qLearner_new, seed) > 0:
            wins += 1
    print("{:.2f}%, {}".format((wins/len(seeds))*100, qLearner_new.weights))

    if wins > base_wins:
        qLearner_base.weights[weight] = qLearner_new.weights[weight]
        base_wins = wins


# Generate a series of losing seeds to test on:
# seeds = []
#
# while len(seeds) < 20:
#     random.seed(time.time())
#     seed = random.randint(0, 100000000000)
#     if run(qLearner_base, seed) <= 0:
#         seeds.append(seed)
#         seeds = list(set(seeds))
#         print("{}: {}".format(len(seeds), seed))
#
#
# print(seeds)