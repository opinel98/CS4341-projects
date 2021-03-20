import sys
import random


sys.path.insert(0, '../bomberman')

# Import necessary stuff
from game import Game
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster
from qlcharacter import qlCharacter
from qlearning import QLearner
from qlhelpers import *
step = 1

qLearner1 = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists],
                    [9.644738825307972, 0.0, -0.7636358419388961, -5.971568757785089, 5.7744223269435375])

qLearner2 = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists],
                    [8.458119902186587, -3.0418798099256046, -0.31907802641410155, -3.770071502872679, 7.126050209167285])

qLearner3 = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists],
                    [8.564012007264198, -3.0569255103512067, 0.06834293304145697, -6.878067177939179, 7.26429976929269])

qLearner4 = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists, f_within_two_of_monster],
                    [6.677040814273156, -2.8712762824080875, 0.0007472148776999527, -0.9223685778177153, 4.6431419153438666e-05, -0.05143683159538506]) # About 78-80%

qLearner5 = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists, f_within_two_of_monster],
                    [6.816656292974258, -2.214658827136486, -0.5886164957366603, -8.324788954040265, 4.402454683798063, 0])

def variant1(g):
    g.add_character(qlCharacter("me",  # name
                                "C",  # avatar
                                0, 0,  # position
                                qLearner1,
                                False,1,1  # variant solution
                                ))
    # Use this if you want to proceed automatically
    g.go(step)
    if g.world.scores["me"] > 0:
        return True


def variant2(g):
    g.add_monster(StupidMonster("stupid",  # name
                                "S",  # avatar
                                3, 9,  # position
                                ))

    g.add_character(qlCharacter("me",  # name
                                "C",  # avatar
                                0, 0,  # position
                                qLearner2,
                                False,1,1
                                ))

    # Run!
    g.go(step)
    if g.world.scores["me"] > 0:
        return True


def variant3(g):
    g.add_monster(SelfPreservingMonster("selfpreserving",  # name
                                        "S",  # avatar
                                        3, 9,  # position
                                        1  # detection range
                                        ))

    g.add_character(qlCharacter("me",  # name
                                "C",  # avatar
                                0, 0,  # position
                                qLearner3,
                                False,1,1
                                ))

    # Run!
    g.go(step)
    if g.world.scores["me"] > 0:
        return True


def variant4(g):
    g.add_monster(SelfPreservingMonster("aggressive",  # name
                                        "A",  # avatar
                                        3, 13,  # position
                                        2  # detection range
                                        ))

    g.add_character(qlCharacter("me",  # name
                                "C",  # avatar
                                0, 0,  # position
                                qLearner4,
                                False,1,1
                                ))

    # Run!
    g.go(step)
    if g.world.scores["me"] > 0:
        return True


def variant5(g):
    g.add_monster(StupidMonster("stupid",  # name
                                "S",  # avatar
                                3, 5,  # position
                                ))
    g.add_monster(SelfPreservingMonster("aggressive",  # name
                                        "A",  # avatar
                                        3, 13,  # position
                                        2  # detection range
                                        ))

    g.add_character(qlCharacter("me",  # name
                                "C",  # avatar
                                0, 0,  # position
                                qLearner5,
                                False,1,1
                                ))

    # Run!
    g.go(step)
    if g.world.scores["me"] > 0:
        return True


def main():
    test_amount = 10
    wins1 = 0
    wins2 = 0
    wins3 = 0
    wins4 = 0
    wins5 = 0
    for _ in range(test_amount):
        g = Game.fromfile('scenario1/map.txt', sprite_dir="../bomberman/sprites/")
        if variant1(g):
            wins1 += 1
    for _ in range(test_amount):
        g = Game.fromfile('scenario1/map.txt', sprite_dir="../bomberman/sprites/")
        if variant2(g):
            wins2 += 1
    for _ in range(test_amount):
        g = Game.fromfile('scenario1/map.txt', sprite_dir="../bomberman/sprites/")
        if variant3(g):
            wins3 += 1
    for _ in range(test_amount):
        g = Game.fromfile('scenario1/map.txt', sprite_dir="../bomberman/sprites/")
        if variant4(g):
            wins4 += 1
    for _ in range(test_amount):
        g = Game.fromfile('scenario1/map.txt', sprite_dir="../bomberman/sprites/")
        if variant5(g):
            wins5 += 1
    print(f'We won {wins1} out of {test_amount} for variant 1')
    print(f'We won {wins2} out of {test_amount} for variant 2')
    print(f'We won {wins3} out of {test_amount} for variant 3')
    print(f'We won {wins4} out of {test_amount} for variant 4')
    print(f'We won {wins5} out of {test_amount} for variant 5')


if __name__ == "__main__":
    # execute only if run as a script
    main()
