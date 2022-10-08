import pygame

class Wall:
    def __init__(self,left,top):
        self.penetrability = False #可穿透性
        self.destructibility = False #可破坏性
        self.live = True

        self.images = {
            'iron' : pygame.image.load('tank/images/ironwall.png'),
            'wood' : pygame.image.load('tank/images/woodwall.png'),
            'grass' : pygame.image.load('tank/images/grasswall.png'),
            'ice' : pygame.image.load('tank/images/icewall.png'),
        }
        self.type = 'iron'
        self.image = self.images[self.type]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top


class IronWall(Wall):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.penetrability = False
        self.destructibility = False
        self.type = 'iron'
        self.image = self.images[self.type]

class WoodWall(Wall):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.penetrability = False
        self.destructibility = True
        self.type = 'wood'
        self.image = self.images[self.type]

class GrassWall(Wall):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.penetrability = True
        self.destructibility = False
        self.type = 'grass'
        self.image = self.images[self.type]

class IceWall(Wall):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.penetrability = True
        self.destructibility = False
        self.type = 'ice'
        self.image = self.images[self.type]
