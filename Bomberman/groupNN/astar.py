# This is necessary to find the main code
import sys
sys.path.insert(0, '../bomberman')
# Import necessary stuff
from entity import CharacterEntity
from real_world import RealWorld

class Node():
    def __init__(self, parent, x, y, g, h):
        self.parent = parent
        self.x =x
        self.y =y
        self.g = g
        self.h = h
        self.f = g + h

class Astar(CharacterEntity, RealWorld):

    def __init__(self, rw):
        self.w = rw
        (self.endx, self.endy) = self.w.exitcell
        self.now = Node(None, 0, 0, 0, 0)
        self.open = []
        self.mx = 0
        self.my = 0

    def findpathtoend(self, sx, sy):
        self.now.x = sx
        self.now.y = sy
        self.open = []
        closed = []
        path = []
        self.now.h = self.distanceToEnd(self.now.x, self.now.y)
        self.now.f = self.now.g + self.now.h
        closed.append(self.now)
        self.addNeighborsToOpen(self.now.x, self.now.y, self.open, closed)
        i = 0
        while(self.now.x != self.endx) or (self.now.y != self.endy):
            if not self.open:
                return None
            self.now = self.open[0]
            self.open.pop(0)
            closed.append(self.now)
            self.addNeighborsToOpen(self.now.x, self.now.y, self.open, closed)
            ++i
        path.insert(0, self.now)
        while(self.now.x != sx) or (self.now.y != sy):
            self.now = self.now.parent
            path.insert(0, self.now)
        path.insert(0, self.now)#esta se puede borrar
        return path

    def distanceToEnd(self, dx, dy):
        return abs(dx - self.endx) + abs(dy - self.endy)

    def findInList(self, list, node):
        for a in list:
            if (a.x == node.x) and (a.y == node.y):
                return True
        return False

    def addNeighborsToOpen(self, lastx, lasty, op, cl):
        for dx in [-1, 0, 1]:
            if(self.now.x + dx >= 0) and (self.now.x + dx < self.w.width()):
                for dy in [-1, 0, 1]:
                    if((dx == 0) and (dy != 0)) or ((dy == 0) and (dx != 0)):
                        if(self.now.y + dy >= 0) and (self.now.y + dy < self.w.height()):
                            if not self.w.wall_at(self.now.x + dx, self.now.y + dy):
                                node = Node(self.now, self.now.x + dx, self.now.y + dy, self.now.g + 1, self.distanceToEnd(self.now.x + dx, self.now.y + dy))
                                if(lastx == self.now.x + dx) and (lasty == self.now.y + dy):
                                    node.f = 0;
                                if (not self.findInList(op, node)) and (not self.findInList(cl, node)):
                                    self.open.append(node)

    def distancetomonster(self, dx, dy):
        m = self.w.monsters[0]
        c = self.w.characters[0]
        return max(abs(m.x - c.x), abs(m.y - c.y))

    def ismonsternear(self):
        for dx in [-1, 0, 1]:
            if(self.now.x + dx >= 0) and (self.now.x + dx < self.w.width()):
                for dy in [-1, 0, 1]:
                    if (dx != 0) or (dy != 0):
                        if(self.now.y + dy >= 0) and (self.now.y + dy < self.w.height()):
                            mons = self.w.monsters_at(self.now.x + dx, self.now.y + dy)
                            if mons:
                                self.mx = dx
                                self.my = dy
                                return True


