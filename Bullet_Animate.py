#This class will inherit from Sprite class too
#I want to keep things in groups and collide with things

#Bullet is a projectile launched by the hunter

import pygame.sprite


class Bullet_Animate(pygame.sprite.Sprite):

    #Bullet being initialized
    #hunter param --> to get position of the hunter and determine how far the bullet should travel
    def __init__(self, x_Val, y_val, bullet_g, hunter):       #x, y val comes from the hunter. The bullet will not be drawn on tile map
        super().__init__()

        # Set constant variables
        self.BULLET_VELOCITY = 20 # 20 pixels per loop in left/right direction.
        self.BULLET_RANGE = 500  #when I create a bullet and moves 500 pixels, it destroys itself after 500 pixels

        # Load image and get rect
        if hunter.hunter_velocity.x > 0:     # > 0 is slash facing left
            self.image = pygame.transform.scale(pygame.image.load("images/player/slash.png"), (32, 32))
        else:
            self.image = pygame.transform.scale(
                pygame.transform.flip(pygame.image.load("images/player/slash.png"), True, False), (32, 32))
            self.BULLET_VELOCITY = -1 * self.BULLET_VELOCITY   #when facing left, we need to negate our velocity

        self.rect = self.image.get_rect()
        self.rect.center = (x_Val, y_val)

        self.starting_xCor = x_Val

        bullet_g.add(self) #adding current bullet to Bullet group

    #As i will move the bullet so the update method handles this
    def update(self):
        self.rect.x += self.BULLET_VELOCITY       #neg or pos depending on Hunter's movement

        # if bullet > RANGE, then it is killed
        #when fired to left, abs is negative.
        if abs(self.rect.x - self.starting_xCor) > self.BULLET_RANGE:   #using abs for absolute val
            self.kill()
