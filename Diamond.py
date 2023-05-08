import pygame.sprite
import pygame, random


#Initializing variable for using 2D vectors
vector = pygame.math.Vector2


#The diamonds that Hunter has to collect to earn points and health
class Diamond(pygame.sprite.Sprite):
    # initializing diamond
    def __init__(self, platform_group, portal_group):
        from main import WIN_WIDTH

        super().__init__()

        # Set constant variables
        self.VERTICAL_ACCELERATION = 3  # Gravity
        self.HORIZONTAL_VELOCITY = 5

        # Animation frames
        self.diamond_spritesList = []

        # Rotating
        self.diamond_spritesList.append(pygame.transform.scale(pygame.image.load("images/ruby/tile001.png"), (64, 64)))
        self.diamond_spritesList.append(pygame.transform.scale(pygame.image.load("images/ruby/tile000.png"), (64, 64)))
        self.diamond_spritesList.append(pygame.transform.scale(pygame.image.load("images/ruby/tile002.png"), (64, 64)))
        self.diamond_spritesList.append(pygame.transform.scale(pygame.image.load("images/ruby/tile003.png"), (64, 64)))
        self.diamond_spritesList.append(pygame.transform.scale(pygame.image.load("images/ruby/tile004.png"), (64, 64)))
        self.diamond_spritesList.append(pygame.transform.scale(pygame.image.load("images/ruby/tile005.png"), (64, 64)))
        self.diamond_spritesList.append(pygame.transform.scale(pygame.image.load("images/ruby/tile006.png"), (64, 64)))

        # Load image and get rect
        self.current_sprite = 0
        self.image = self.diamond_spritesList[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WIN_WIDTH // 2, 100)

        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group

        # Load sounds
        self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")

        # Kinematic vectors
        # DIAMOND moves under gravity
        self.position = vector(self.rect.x, self.rect.y)
        self.velocity = vector(random.choice([-1 * self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY]), 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

    # This updates the diamond
    # This is from the Sprite update method
    def update(self):
        self.animate_diamond(self.diamond_spritesList, .25)
        self.move()
        self.check_diamond_collisions() #The diamond will move

    def move(self):
        from main import WIN_WIDTH
        # We don't need to update the accelreation vector because it never changes here

        # Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        # Update rect based on kinematic calculations and add wrap around movement
        if self.position.x < 0:
            self.position.x = WIN_WIDTH
        elif self.position.x > WIN_WIDTH:
            self.position.x = 0

        self.rect.bottomleft = self.position

    #Check collisions with platforms and portals
    def check_diamond_collisions(self):
        from main import WIN_WIDTH, WIN_HEIGHT
        # Collision check between ruby and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0

        # Collision check for portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.portal_sound.play()
            # Determine which portal you are moving to
            # Left and right
            if self.position.x > WIN_WIDTH // 2:
                self.position.x = 86
            else:
                self.position.x = WIN_WIDTH - 150
            # Top and bottom
            if self.position.y > WIN_HEIGHT // 2:
                self.position.y = 64
            else:
                self.position.y = WIN_HEIGHT - 132

            self.rect.bottomleft = self.position


    #this wil animate the diamond
    def animate_diamond(self, sprite_list, speed):
      if self.current_sprite < len(sprite_list) -1:
        self.current_sprite += speed
      else:
        self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]