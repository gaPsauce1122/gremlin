#THIS CLASS IS FOR 32 X 32 PIXEL AREA IN OUR GAME DISPLAY
import pygame

class TileMapping(pygame.sprite.Sprite):
    """A class to represent a 32x32 pixel area in our display"""

    def __init__(self, xcor, ycor, tile_pic_int, main_group, sub_group=""):
        """Initialize the tile"""
        super().__init__()
        # Load in the correct image and add it to the correct sub group
        # Dirt tiles
        if tile_pic_int == 1:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (1).png"), (32, 32))
        # Platform tiles
        elif tile_pic_int == 2:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (2).png"), (32, 32))
            sub_group.add(self)
        elif tile_pic_int == 3:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (3).png"), (32, 32))
            sub_group.add(self)
        elif tile_pic_int == 4:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (4).png"), (32, 32))
            sub_group.add(self)
        elif tile_pic_int == 5:
            self.image = pygame.transform.scale(pygame.image.load("images/tiles/Tile (5).png"), (32, 32))
            sub_group.add(self)

        # every tile is added to the main_group
        main_group.add(self)

        # Get the rect of the image and position within the grid
        self.rect = self.image.get_rect()
        self.rect.topleft = (xcor, ycor) #topleft --> r, c are multiples of 32. when r,c is 0 (x,y)= (0,0) which is topleft of game window

        # Create a mask for better hunter collisions
        self.mask = pygame.mask.from_surface(self.image)