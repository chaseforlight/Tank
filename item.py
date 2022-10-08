import pygame
import random
from game_values import GameValue

class Item:
    def __init__(self):
        self.images = {
            'add_bullet' : pygame.image.load('tank/images/add_bullet_item.png'),
            'protect_myself' : pygame.image.load('tank/images/protect_myself_item.png')
        }
        self.type = 'add_bullet'
        self.image = self.images[self.type]
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = self.rankPosition()

        self.frequency = 0.01 #道具出现频率，1 表示 100%

        self.live = True

    def displayItem(self):
        self.image = self.images[self.type]
        GameValue.window.blit(self.image,self.rect)

    def rankPosition(self):
        left = random.randint(0,1176)
        top = random.randint(0,876)
        return left,top

    def rankShow(self):
        random_number = random.randint(1,10000) / 10000
        if random_number <= self.frequency:
            GameValue.item_list.append(self)

    def myTank_eat_item(self):
        if pygame.sprite.collide_rect(self,GameValue.my_tank):
            self.live = False
            self.make_effect()
            
    def make_effect(self):
        pass

class AddBulletItem(Item):
    def __init__(self):
        super().__init__()
        self.type = 'add_bullet'
        self.frequency = 0.002
    def make_effect(self):
        GameValue.max_bullet_num += 1

class ProtectMyselfItem(Item):
    def __init__(self):
        super().__init__()
        self.type = 'protect_myself'
        self.frequency = 0.002
    def make_effect(self):
        pass
    
