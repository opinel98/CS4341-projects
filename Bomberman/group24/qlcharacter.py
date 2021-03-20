# This is necessary to find the main code
import sys
import random, math
import heapq
from qlhelpers import *
from colorama import Fore, Back

sys.path.insert(0, '../bomberman')
# Import necessary stuff
from entity import CharacterEntity
from sensed_world import SensedWorld


class qlCharacter(CharacterEntity):
    def __init__(self, name, avatar, x, y, qLearner, isTraining, iNum, maxI, bombs = True):
        CharacterEntity.__init__(self, name, avatar, x, y)
        self.exit = None
        self.bombed = None
        self.squares = {}

        self.qLearner = qLearner
        self.isTraining = isTraining
        self.iNum = iNum
        self.maxI = maxI

        self.ranChance = 1 / (self.iNum + 1) ** .5
        self.bombs = bombs
        self.previousWorld = None

    def do(self, wrld):
        self.previousWorld = wrld
        self.squares = {}

        if self.isTraining:
            if random.random() < self.randomChance:
                ranStep = [-1, 0, 1]

                if self.bombs:
                    posBomb = [0, 1]
                else:
                    posBomb = [0]

                if random.choice(posBomb) == 1:
                    self.place_bomb()

                dx = random.choice(ranStep)
                dy = random.choice(ranStep)

                self.move(dx, dy)
            else:
                move, _ = self.qLearner.bestMove(wrld, self)
                dx, dy, bomb = move

                self.move(dx, dy)

                if bomb == 1:
                    self.place_bomb()
        else:
            move, _ = self.qLearner.bestMove(wrld, self)
            dx, dy, bomb = move
            self.move(dx, dy)

            if bomb == 1:
                self.place_bomb()

    def updateWeights(self, wrld, won, lost):
        if self.isTraining:
            if won:
                r = 100
            elif lost:
                r = -50
            else:
                r = (f_to_exit(wrld, self)**.1)*10 - (f_to_monster(wrld, self)**.1)*5

            self.qLearner.updateWeights(self.previousWorld, wrld, self, r)