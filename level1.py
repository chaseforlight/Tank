from wall import *

def createLevel1():
    wall_list = []
    for left in range(212,1100,246):
        for top in range(0,110,34):
            wall = GrassWall(left,top)
            wall_list.append(wall)

    top = 100
    for left in range(0,1200,34):
        wall = GrassWall(left,top)
        wall_list.append(wall)
    
    left = 250
    for top in range(134,900,34):
        wall = GrassWall(left,top)
        wall_list.append(wall)

    left = 880
    for top in range(134,900,34):
        wall = GrassWall(left,top)
        wall_list.append(wall)

    for top in range(300,710,200):
        for left in range(0,250,34):
            wall = GrassWall(left,top)
            wall_list.append(wall)
        for left in range(914,1200,34):
            wall = GrassWall(left,top)
            wall_list.append(wall)
    
    for top in range(200,810,200):
        for left in range(284,890,34):
            wall = GrassWall(left,top)
            wall_list.append(wall)
    return wall_list
    
