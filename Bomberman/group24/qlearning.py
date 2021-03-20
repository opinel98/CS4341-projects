import sys
from qlhelpers import *

sys.path.insert(0, "../")

from entity import *
from events import Event

from sensed_world import SensedWorld

G = .9
A = .2

class QLearner:
    def __init__(self, funcs, weights=[], bombs=True):
        self.funcs = funcs
        if weights == []:
            self.weights = [0]*len(self.funcs)
        else:
            self.weights = weights

        if not bombs:
            self.possibleMoves = [(1, 0, 0), (1, 1, 0), (1, -1, 0), (-1, 0, 0), (-1, 1, 0), (-1, -1, 0), (0, -1, 0), (0, 1, 0), (0, 0, 0)]
        else:
            self.possibleMoves = [(1, 0, 0), (1, 1, 0), (1, -1, 0), (-1, 0, 0), (-1, 1, 0), (-1, -1, 0), (0, -1, 0), (0, 1, 0), (0, 0, 0),
                                  (1, 0, 1), (1, 1, 1), (1, -1, 1), (-1, 0, 1), (-1, 1, 1), (-1, -1, 1), (0, -1, 1), (0, 1, 1), (0, 0, 1)]

    # returns (dx, dy, bomb?)
    def bestMove(self, wrld, character):
        max_a = (0, 0, 0)
        max_q = -9999
        for pMove in self.possibleMoves:
            newWorld = SensedWorld.from_world(wrld)

            if newWorld.me(character) is None:
                continue

            newWorld.me(character).move(pMove[0], pMove[1])
            if pMove[2] == 1:
                newWorld.me(character).place_bomb()

            newWorld, events = newWorld.next()

            if newWorld.me(character) is None:
                for event in events:
                    if event.tpe == Event.BOMB_HIT_CHARACTER or event.tpe == Event.CHARACTER_KILLED_BY_MONSTER:
                        q = -9999
                    if event.tpe == Event.CHARACTER_FOUND_EXIT:
                        q = 9999
            else:
                q = self.Q(newWorld, newWorld.me(character))

            if q > max_q:
                max_a = pMove
                max_q = q

        return (max_a, max_q)

    def updateWeights(self, prevWorld, newWorld, character, reward):
        delta = (reward) - self.Q(newWorld, character)

        for i in range(len(self.funcs)):
            self.weights[i] += A * delta * self.funcs[i](newWorld, character)

    def Q(self, world, character):
        sum = 0

        for i in range(len(self.funcs)):
            sum += self.weights[i] * self.funcs[i](world, character)

        return sum
