from wall import *
from game_values import GameValue

def createLevelTest():
    wall_list = []
    top = 400
    for left in range(0,1100,17):
        wall = GrassWall(left,top)
        wall_list.append(wall)
    top = 434
    for left in range(0,1100,17):
        wall = GrassWall(left,top)
        wall_list.append(wall)
    left = 300
    for top in range(560,900,17):
        wall = IceWall(left,top)
        wall_list.append(wall)
    left = 700
    for top in range(560,900,17):
        wall = IronWall(left,top)
        wall_list.append(wall)
    top = 300
    for left in range(100,1200,17):
        wall = WoodWall(left,top)
        wall_list.append(wall)
    return wall_list
