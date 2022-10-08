import sys
import pygame
from time import sleep
import random
from game_values import GameValue
from wall import *
from bullet import Bullet
from explode import Explode
from pen import Pen
from tank import Tank,EnemyTank
from item import *
from button import Button
from level1 import createLevel1
from leveltest import createLevelTest

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

class MainGame:
    def __init__(self):
        pass
    def startGame(self):
        #游戏初始化
        pygame.init()
        self.initWindow()
        self.initTank()
        self.initWall()
        self.createButton()
        #游戏循环
        while True:
            sleep(0.02)

            GameValue.window.fill('black')
            self.getEvent()

            if not GameValue.game_over:
                self.blitMyTank()
                self.blitEnemyTank() 
                self.blitMyBullet()
                self.blitEnemyBullet()
                self.blitExplode()
                self.blitWall()
                self.randomCreateItem()
                self.blitItem()

                if not GameValue.my_tank.stop:
                    GameValue.my_tank.move()
            else:
                self.blitGameOverText()
                self.blitButton()

            pygame.display.update()

    def endGame(self):
        pygame.quit()
        sys.exit()

    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    GameValue.my_tank.direction = 'L'
                    GameValue.my_tank.stop = False
                elif event.key == pygame.K_RIGHT:
                    GameValue.my_tank.direction = 'R'
                    GameValue.my_tank.stop = False
                elif event.key == pygame.K_UP:
                    GameValue.my_tank.direction = 'U'
                    GameValue.my_tank.stop = False
                elif event.key == pygame.K_DOWN:
                    GameValue.my_tank.direction = 'D'
                    GameValue.my_tank.stop = False
                elif event.key == pygame.K_SPACE:
                    if len(GameValue.my_bullet_list) < GameValue.max_bullet_num:
                        mybullet =  Bullet(GameValue.my_tank)
                        GameValue.my_bullet_list.append(mybullet)
                elif event.key == pygame.K_q:
                    self.endGame()
                elif event.key == pygame.K_p:
                    self.restartGame()

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT 
                    or event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    GameValue.my_tank.stop = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if GameValue.button.check_click(mouse_pos):
                    self.restartGame()
    
    def createEnemyTank(self):
        # for i in range(GameValue.enemy_tank_num):
        #     left = random.randint(0,1150)
        #     top = random.randint(0,200)
        #     speed = random.randint(3,5)
        #     enemy = EnemyTank(left,top,speed)
        #     GameValue.enemy_tank_list.append(enemy)

        while(len(GameValue.enemy_tank_list) < GameValue.enemy_tank_num):
            left = random.randint(0,1150)
            top = random.randint(0,200)
            speed = random.randint(3,5)
            enemyTank = EnemyTank(left,top,speed)
            can_be_placed_here = True
            for otherTank in GameValue.enemy_tank_list:
                if enemyTank.tank_hit_tank() or enemyTank.tank_hit_wall():
                    can_be_placed_here = False
            if can_be_placed_here:
                GameValue.enemy_tank_list.append(enemyTank)

    def createWall(self):
        GameValue.wall_list =  createLevel1()

    def randomCreateItem(self):
        add_bullet_item = AddBulletItem()
        add_bullet_item.rankShow()

    def createButton(self):
        GameValue.button = Button()

    def blitEnemyTank(self):
        if len(GameValue.enemy_tank_list) == 0:
            GameValue.game_over = True
            GameValue.lose_or_win = 1
        else:
            for enemyTank in GameValue.enemy_tank_list:
                if enemyTank.live:
                    enemyTank.displayTank()
                    enemyTank.randMove()
                    enemy_bullet =  enemyTank.shot()
                    if enemy_bullet != None:
                        GameValue.enemy_bullet_list.append(enemy_bullet)
                else:
                    GameValue.enemy_tank_list.remove(enemyTank)

    def blitMyTank(self):
        if GameValue.my_tank.live:
            GameValue.my_tank.displayTank()
        else:
            GameValue.game_over = True
            GameValue.lose_or_win = 0

    def blitMyBullet(self):
        for mybullet in GameValue.my_bullet_list:
            if mybullet.live:
                mybullet.displayBullet()
                mybullet.move()
                mybullet.myBullet_hit_enemyTank()
                mybullet.bullet_hit_wall()
                mybullet.myBullet_hit_enemyBullet()
            else:
                GameValue.my_bullet_list.remove(mybullet)

    def blitEnemyBullet(self):
        for enemybullet in GameValue.enemy_bullet_list:
            if enemybullet.live:
                enemybullet.displayBullet()
                enemybullet.move()
                enemybullet.enemyBullet_hit_myTank()
                enemybullet.bullet_hit_wall()   
            else:
                GameValue.enemy_bullet_list.remove(enemybullet)

    def blitExplode(self):
        for explode in GameValue.explore_list:
            if explode.live:
                explode.displayExplode()
            else:
                GameValue.explore_list.remove(explode)

    def blitGameOverText(self):
        text = Pen(GameValue.lose_or_win)
        text.displayText()

    def blitWall(self):
        for wall in GameValue.wall_list:
            if wall.live:
                GameValue.window.blit(wall.image,wall.rect)
            else:
                GameValue.wall_list.remove(wall)

    def blitItem(self):
        for item in GameValue.item_list:
            if item.live:
                item.displayItem()
                item.myTank_eat_item()
            else:
                GameValue.item_list.remove(item)

    def blitButton(self):
        GameValue.button.displayButton()

    def initWindow(self):
        # pygame.init()
        GameValue.window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('坦克大战')

    def initTank(self):
        GameValue.my_tank = Tank(500,800)
        GameValue.enemy_tank_list = []
        GameValue.enemy_bullet_list = []
        GameValue.my_bullet_list = []
        GameValue.explore_list = []
        self.createEnemyTank()

    def initWall(self):
        self.createWall()

    def initItem(self):
        GameValue.item_list = []

    def restartGame(self):
        GameValue.game_over = False
        self.initTank()
        self.initWall()
        self.initItem()   


if __name__ == '__main__':
    mg = MainGame()
    mg.startGame()
