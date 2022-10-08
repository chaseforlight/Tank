import pygame
import random
from game_values import GameValue
from base_item import BaseItem
from bullet import Bullet

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

class Tank(BaseItem):
    def __init__(self,left,top):
        self.images  = {
            'U' : pygame.image.load('tank/images/tankup.png'),
            'D' : pygame.image.load('tank/images/tankdown.png'),
            'L' : pygame.image.load('tank/images/tankleft.png'),
            'R' : pygame.image.load('tank/images/tankright.png'),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

        self.speed = 8
        self.stop = True

        self.live = True


    def move(self):
        is_hit = self.tank_hit_wall() or self.tank_hit_tank()
        if self.direction == 'U':
            if(self.rect.top > 0 and is_hit == False):
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if(self.rect.top + self.rect.height < SCREEN_HEIGHT and is_hit == False):
                self.rect.top += self.speed
        elif self.direction == 'R':
            if(self.rect.left + self.rect.width < SCREEN_WIDTH and is_hit == False):
                self.rect.left += self.speed
        elif self.direction == 'L':
            if(self.rect.left > 0 and is_hit == False):
                self.rect.left -= self.speed
        
    def displayTank(self):
        self.image = self.images[self.direction]
        GameValue.window.blit(self.image,self.rect)

    def shot(self):
        return Bullet(self)

    def make_offset_copy(self):
        copy_rect = pygame.Rect.copy(self.rect)
        if self.direction == 'U': #之所以这样写，是因为防止一发生碰撞就再也无法动弹的情况，且需满足偏移量大于步长
            copy_rect.top -= 10
        elif self.direction == 'D':
            copy_rect.top += 10
        elif self.direction == 'R':
            copy_rect.left += 10
        elif self.direction == 'L':
            copy_rect.left -= 10
        return copy_rect

    def tank_hit_wall(self):
        result = False #表示未发生碰撞
        copy_rect = self.make_offset_copy()

        for wall in GameValue.wall_list:
            if wall.penetrability == False:
                if pygame.Rect.colliderect(copy_rect,wall.rect):
                    result = True # 表示发生碰撞
        return result

    def tank_hit_tank(self):
        result = False
        copy_rect = self.make_offset_copy()

        if GameValue.my_tank != self:
            if pygame.Rect.colliderect(copy_rect,GameValue.my_tank.rect):
                result = True
        for enemyTank in GameValue.enemy_tank_list:
            if enemyTank != self:
                if pygame.Rect.colliderect(copy_rect,enemyTank.rect):
                    result = True
                    break
        return result


class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        self.images  = {
            'U' : pygame.image.load('tank/images/enemytankup.png'),
            'D' : pygame.image.load('tank/images/enemytankdown.png'),
            'L' : pygame.image.load('tank/images/enemytankleft.png'),
            'R' : pygame.image.load('tank/images/enemytankright.png'),
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.stop = True
        self.steps = 80

        self.live = True

    def randDirection(self):
        return random.choice(['U','D','L','R'])
    def randMove(self):
        if self.steps <= 0:
            self.direction = self.randDirection()
            self.steps = random.randint(30,120)
        else:
            self.move()
            self.steps -= 1

    def shot(self):
        num = random.randint(0,100)
        if num < 30:
            return Bullet(self)
        else:
            return None

    def enemyTank_hit_wall(self):
        pass
