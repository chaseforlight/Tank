import pygame
from game_values import GameValue

class Pen:
    def __init__(self,textmode):
        self.texts = ['YOU LOSE!','YOU WIN!']
        self.textmode = textmode

        self.font_name = 'arial'
        self.font = pygame.font.SysFont(self.font_name,50)
        self.text = self.font.render(self.texts[self.textmode],True,'red')
        self.textRect = self.text.get_rect()
        self.textRect.center = (600,450)

    def displayText(self):
        GameValue.window.blit(self.text,self.textRect)
