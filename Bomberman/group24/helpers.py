import math
import heapq

INFINITY = float("inf")


# Determine the x component of the distance to the closest exit
# Note: closest is determined using both x and y components
def x_distance_to_exit(world, character):
    character_location = (character.x, character.y)

    exits = find_exits(world)

    if len(exits) == 0:
        return INFINITY

    closest_exit = closest_point(character_location, exits)
    return closest_exit[0] - character_location[0]


# Determine the y component of the distance to the closest exit
# Note: closest is determined using both x and y components
def y_distance_to_exit(world, character):
    character_location = (character.x, character.y)

    exits = find_exits(world)

    if len(exits) == 0:
        return INFINITY

    closest_exit = closest_point(character_location, exits)
    return closest_exit[1] - character_location[1]


# Determine the x component of the distance to the closest monster
# Note: closest is determined using both x and y components
def x_distance_to_monster(world, character):
    character_location = (character.x, character.y)

    monsters = find_monsters(world)

    if len(monsters) == 0:
        return INFINITY

    closest_monster = closest_point(character_location, monsters)
    return closest_monster[0] - character_location[0]


# Determine the y component of the distance to the closest monster
# Note: closest is determined using both x and y components
def y_distance_to_monster(world, character):
    character_location = (character.x, character.y)

    monsters = find_monsters(world)

    if len(monsters) == 0:
        return INFINITY

    closest_monster = closest_point(character_location, monsters)
    return closest_monster[1] - character_location[1]


# Determine the x component of the distance to the closest bomb
# Note: closest is determined using both x and y components
def x_distance_to_bomb(world, character):
    character_location = (character.x, character.y)

    bombs = find_bombs(world)

    if len(bombs) == 0:
        return INFINITY

    closest_bomb = closest_point(character_location, bombs)
    return closest_bomb[0] - character_location[0]


# Determine the y component of the distance to the closest bomb
# Note: closest is determined using both x and y components
def y_distance_to_bomb(world, character):
    character_location = (character.x, character.y)

    bombs = find_bombs(world)

    if len(bombs) == 0:
        return INFINITY

    closest_bomb = closest_point(character_location, bombs)
    return closest_bomb[1] - character_location[1]


# Determine the x component of the distance to the closest wall
# Note: closest is determined using both x and y components
def x_distance_to_wall(world, character):
    character_location = (character.x, character.y)

    walls = find_walls(world)

    if len(walls) == 0:
        return INFINITY

    closest_wall = closest_point(character_location, walls)
    return closest_wall[0] - character_location[0]


# Determine the y component of the distance to the closest wall
# Note: closest is determined using both x and y components
def y_distance_to_wall(world, character):
    character_location = (character.x, character.y)

    walls = find_walls(world)

    if len(walls) == 0:
        return INFINITY

    closest_wall = closest_point(character_location, walls)
    return closest_wall[1] - character_location[1]


# Return the number of walls in the world
def num_walls(world):
    return len(find_walls(world))


# Determine the x direction for the next step in the optimal path
# from the character's current location to the nearest exit
# Note: closest is determined using both x and y components
def a_star_next_x(world, character):
    character_location = (character.x, character.y)

    exits = find_bombs(world)

    if len(exits) == 0:
        return INFINITY

    closest_exit = closest_point(character_location, exits)
    next_position = a_star(world, character_location, closest_exit)[0][1]

    x_diff = next_position[0] - character_location[0]

    if x_diff == 0:
        return 0
    elif x_diff < 0:
        return -1
    else:
        return 1


# Determine the y direction for the next step in the optimal path
# from the character's current location to the nearest exit
# Note: closest is determined using both x and y components
def a_star_next_y(world, character):
    character_location = (character.x, character.y)

    exits = find_bombs(world)

    if len(exits) == 0:
        return INFINITY

    closest_exit = closest_point(character_location, exits)
    next_position = a_star(world, character_location, closest_exit)[0][1]

    y_diff = next_position[1] - character_location[1]

    if y_diff == 0:
        return 0
    elif y_diff < 0:
        return -1
    else:
        return 1

##################
# UTILITIES ######
##################


# Find any exits in the world
def find_exits(world):
    exits = []
    for x in range(0, world.width()):
        for y in range(0, world.height()):
            if world.exit_at(x, y):
                exits.append((x, y))
    return exits


# Find any monsters in the world
def find_monsters(world):
    monsters = []
    for x in range(0, world.width()):
        for y in range(0, world.height()):
            if world.monsters_at(x, y):
                monsters.append((x, y))
    return monsters


# Find any bombs in the world
def find_bombs(world):
    bombs = []
    for x in range(0, world.width()):
        for y in range(0, world.height()):
            if world.bomb_at(x, y):
                bombs.append((x, y))
    return bombs


# Find any walls in the world
def find_walls(world):
    walls = []
    for x in range(0, world.width()):
        for y in range(0, world.height()):
            if world.wall_at(x, y):
                walls.append((x, y))
    return walls


# Find any explosions in the world
def find_explosions(world):
    expls = []
    for x in range(0, world.width()):
        for y in range(0, world.height()):
            if world.explosion_at(x, y):
                expls.append((x, y))
    return expls

# Given a point p1, find the closest point in points to p1
# If euclidean is True, use euclidean distance, otherwise use manhattan distance
def closest_point(p1, points, euclidean=True):
    closest = points[0]

    for point in points:
        if euclidean:
            if euclidean_distance_between(p1, point) < euclidean_distance_between(p1, closest):
                closest = point
        else:
            if manhattan_distance_between(p1, point) < manhattan_distance_between(p1, closest):
                closest = point
    return closest


# Determine the euclidean distance between two points
def euclidean_distance_between(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# Determine the manhattan distance between two point
def manhattan_distance_between(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Find the optimal path between start and end in the world and return the path
# Note: the first point in the path will be the starting point
def a_star(world, start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            break

        for direction in [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]:
            next = (current[0] + direction[0], current[1] + direction[1])
            if next[0] < 0 or next[0] >= world.width() or next[1] < 0 or next[1] >= world.height():
                continue
            if world.wall_at(next[0], next[1]):
                cost = 10
            else:
                cost = 1

            new_cost = cost_so_far[current] + cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + manhattan_distance_between(end, next)
                frontier.put(next, priority)
                came_from[next] = current
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return (path, cost_so_far[end])


# From RedBlobGames
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]