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

qLearner1 = QLearner([f_to_exit, f_is_exploded_now, f_bomb_to_wall, f_time_to_explosion], [157.52129963352013, -65.41935486086436, 28.856877994965103, 20.48922401645315])

qLearner2 = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [163.74500850965978, -74.81375861611413, -3.710392437626575, 26.26781955724994, 71.22790728981906, 42.2166434790756, 3.47072116678088])

qLearner3 = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [169.5792884684401, -89.43359914000227, -9.055797124970724, 5.3165976373538, 100.30312257082886, 71.41381770528874, 4.911815807943525])

qLearner4 = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [159.33304471198795, -78.09792999957172, -18.750314892480493, 5.0167239427069035, 121.1905955320059, 124.59454062803833, 3.716190063440644])

qLearner5 = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [164.12592154785062, -72.35351066390663, -18.986104409901127, 8.473394337312714, 218.7488044723275, 224.56932851491754, 1.7431601829087855])


def variant1(g):
    g.add_character(qlCharacter("me",  # name
                                "C",  # avatar
                                0, 0,
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
                                3, 9  # position
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
    wins1_2 = 0
    wins2_2 = 0
    wins3_2 = 0
    wins4_2 = 0
    wins5_2 = 0
    for _ in range(test_amount):
        g = Game.fromfile('scenario2/map.txt', sprite_dir="../bomberman/sprites/")
        if variant1(g):
            wins1_2 += 1
    for _ in range(test_amount):
        g = Game.fromfile('scenario2/map.txt', sprite_dir="../bomberman/sprites/")
        if variant2(g):
            wins2_2 += 1
    for _ in range(test_amount):
        g = Game.fromfile('scenario2/map.txt', sprite_dir="../bomberman/sprites/")
        if variant3(g):
            wins3_2 += 1
    for _ in range(test_amount):
        g = Game.fromfile('scenario2/map.txt', sprite_dir="../bomberman/sprites/")
        if variant4(g):
            wins4_2 += 1
    for _ in range(test_amount):
        g = Game.fromfile('scenario2/map.txt', sprite_dir="../bomberman/sprites/")
        if variant5(g):
            wins5_2 += 1
    print(f'We won {wins1_2} out of {test_amount} for variant 1_2')
    print(f'We won {wins2_2} out of {test_amount} for variant 2_2')
    print(f'We won {wins3_2} out of {test_amount} for variant 3_2')
    print(f'We won {wins4_2} out of {test_amount} for variant 4_2')
    print(f'We won {wins5_2} out of {test_amount} for variant 5_2')


if __name__ == "__main__":
    # execute only if run as a script
    main()