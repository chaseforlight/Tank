import pygame
from game_values import GameValue

class Explode:
    def __init__(self,tank):
        self.rect = tank.rect
        self.images = [
            pygame.image.load('tank/images/explode1.png'),
            pygame.image.load('tank/images/explode2.png'),
            pygame.image.load('tank/images/explode3.png'),
            pygame.image.load('tank/images/explode4.png'),
            pygame.image.load('tank/images/explode5.png'),
        ]
        self.step = 0
        self.image = self.images[self.step]

        #让图片消失
        self.live = True

    def displayExplode(self):
        #根据索引获取爆炸图片
        if self.step < len(self.images):
            self.image = self.images[self.step]
            self.step += 1
            #添加到主窗口
            GameValue.window.blit(self.image,self.rect)
        else:
            #修改状态
            self.live = False
            self.step = 0
