import pygame
import random

#If you collide with it you will be transported
class Game_portals(pygame.sprite.Sprite):
    # initializing portals
    def __init__(self, xcor, ycor, portal_color, game_portal_group):
        super().__init__()

        # blank list to hold all the images of portals. Animation frames
        self.portal_animation_sprites_list = []

        #animating the portals in the game display. checking the colors if green or purple
        if portal_color == "green":
            #Green portal
            #originally portals are 64 x 64. i increased it to 72 x 72
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile000.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile001.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile002.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile003.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile004.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile005.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile006.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile007.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile008.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile009.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile010.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile011.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile012.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile013.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile014.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile015.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile016.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile017.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile018.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile019.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile020.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/green/tile021.png"), (72,72)))
        else:
            #Purple portal
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile000.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile001.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile002.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile003.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile004.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile005.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile006.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile007.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile008.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile009.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile010.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile011.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile012.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile013.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile014.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile015.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile016.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile017.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile018.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile019.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile020.png"), (72,72)))
            self.portal_animation_sprites_list.append(pygame.transform.scale(pygame.image.load("images/portals/purple/tile021.png"), (72,72)))

        # This step loads the image to the and get a rect to position it
        self.current_portal_spriteList_index = random.randint(0, len(self.portal_animation_sprites_list) - 1)
        self.image = self.portal_animation_sprites_list[self.current_portal_spriteList_index]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (xcor, ycor)

        # Add to the portal group
        game_portal_group.add(self)

    # This updates the portals
    # This is from the Sprite update method
    def update(self):
        self.animate_portals(self.portal_animation_sprites_list, .2)

    # this wil animate the portal
    def animate_portals(self, portal_sprite_list, animation_speed):
        """Portals are animated"""
        if self.current_portal_spriteList_index < len(portal_sprite_list) - 1:
            self.current_portal_spriteList_index += animation_speed
        else:
            self.current_portal_spriteList_index = 0

        self.image = portal_sprite_list[int(self.current_portal_spriteList_index)]
