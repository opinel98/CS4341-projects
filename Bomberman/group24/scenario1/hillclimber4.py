# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

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
    g.add_monster(SelfPreservingMonster("monster",  # name
                                        "M",  # avatar
                                        3, 13,  # position
                                        2  # detection range
                                        ))

    g.add_character(qlCharacter("me",  # name
                               "C",  # avatar
                               0, 0,  # position
                               learner,
                               False, 0, 0))

    # Run!
    g.go()
    return g.world.scores["me"]


functions = [f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists, f_within_two_of_monster]



qLearner_base = QLearner(functions,
                         [6.677040814273156, -2.8712762824080875, -0.0007472148776999527, -0.9223685778177153, -4.6431419153438666e-05, -0.05143683159538506])
#[35.8728849892065, -13.837356743173592, 0.0016751148444334532, -1.627936404499567, 3.766290174603711e-05, -0.0826268186315153])
# ^ ~74% win rate
#[135.78997983273706, -13.837356743173592, -1.9591822542083817, -40.30393572524584, -0.8619557634513888, -11.497689480517705])
# ^ ~42% win rate

'''seeds = [16125028736, 93750928222, 44623792376, 52462414967, 53006102392, 98275871204, 76529262575, 6969420561,
         68525464697, 72349058938, 42216982284, 84573201665, 32556692762, 69661862793, 71890340874, 26510833055,
         18277275557, 61089522450, 57561524116, 84373097993, 83052405775, 23983780907, 15416488494, 543310013,
         32905235637, 62501764776, 43674904498, 74856896422, 46904833464, 98860955935, 58517105379, 41117498688,
         72634425143, 77492829242, 80842421179, 10140840930, 80379275202, 57652912846, 82269331393, 38169461467,
         54443225428, 63723308241, 89403586117, 12392862187, 33370496996, 17724921580, 52245509215, 10006337013,
         79292690391, 9472837498]'''

seeds = [39385742958, 63612339144, 28770774873, 53722702222, 39942684697, 96723284511, 88711075202, 39050539676, 12441279978, 24433744261, 58554312661, 83421859191, 42815969832, 61318179194, 80885972468, 53735835809, 84817842484, 15313479029, 46475636360, 55230689637]

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

'''
# Generate a series of losing seeds to test on:
seeds = []

while len(seeds) < 20:
    random.seed(time.time())
    seed = random.randint(0, 100000000000)
    if run(qLearner_base, seed) <= 0:
        seeds.append(seed)
        seeds = list(set(seeds))
        print("{}: {}".format(len(seeds), seed))
        '''

print(seeds)
