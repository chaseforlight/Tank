import pygame
from game_values import GameValue

class Button:
    def __init__(self):
        self.font_name = 'arial'
        self.font = pygame.font.SysFont(self.font_name,50)
        self.msg = 'Play'
        self.text = self.font.render(self.msg,True,'yellow')
        self.rect = self.text.get_rect()
        self.rect.center = (600,600)

    def displayButton(self):
        GameValue.window.blit(self.text,self.rect)

    def check_click(self,mouse_pos):
        if GameValue.button.rect.collidepoint(mouse_pos):
            return True
        else:
            return False
