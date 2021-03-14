# This is necessary to find the main code
import sys
sys.path.insert(0, '../bomberman')
# Import necessary stuff
from entity import CharacterEntity
from astar import Astar
from colorama import Fore, Back

class OurCharacter(CharacterEntity):

    def __init__(self, n, d, x, y, wrld):
        CharacterEntity.__init__(self, n, d, x, y)
        #self.pathMaker = Astar(wrld)
        #self.path = self.pathMaker.findpathtoend(self.x, self.y)
        #print('path length: ', len(self.path))
        self.path = self.makepath(wrld)
        self.i = 0

    def makepath(self, wrld):
        pathMaker = Astar(wrld)
        return pathMaker.findpathtoend(self.x, self.y)

    def do(self, wrld):
        bomb = False
        self.move(self.path[self.i + 1].x - self.path[self.i].x, self.path[self.i + 1].y - self.path[self.i].y)
 #       for i in path:
  #          self.move(i.x, i.y)
   #         print('Ind: ', ind, 'X: ', i.x, 'Y: ', i.y)
    #        ++ind
     #       if(ind > 7):
      #          break
        if bomb:
            self.place_bomb()
        self.i = self.i + 1

    def printpath(self, path):
        for i in path:
            print('X: ', i.x, 'Y: ', i.y)
