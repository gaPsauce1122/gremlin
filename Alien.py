import pygame, random

#Initializing variable for using 2D vectors
vector = pygame.math.Vector2

class Alien(pygame.sprite.Sprite):

    # initializing aliens
    def __init__(self,platform_group, portal_group, min_speed, max_speed):
        from main import WIN_WIDTH, WIN_HEIGHT
        super().__init__()

        # Set constant variables
        self.GREMLIN_VERTICAL_ACCELERATION = 3  # Gravity
        self.RISE_TIME = 2 #if we dont collide qith the gremlins after we kill, it will come back to life

        # Animation frames
        self.spritesList_walk_right = []
        self.spritesList_walk_left = []
        self.spritesList_die_right = []
        self.spritesList_die_left = []
        self.spritesList_rise_right = []
        self.spritesList_rise_left = []

        gender = random.randint(0, 1)
        if gender == 0:
            # Walking
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (1).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (2).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (3).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (4).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (5).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (6).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (7).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (8).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (9).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/walk/Walk (10).png"), (64, 64)))
            for sprite in self.spritesList_walk_right:
                self.spritesList_walk_left.append(pygame.transform.flip(sprite, True, False))

            # Dying
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (1).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (2).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (3).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (4).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (5).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (6).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (7).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (8).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (9).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (10).png"), (64, 64)))
            for sprite in self.spritesList_die_right:
                self.spritesList_die_left.append(pygame.transform.flip(sprite, True, False))

            # Rising
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (10).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (9).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (8).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (7).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (6).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (5).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (4).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (3).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (2).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/boy/dead/Dead (1).png"), (64, 64)))
            for sprite in self.spritesList_rise_right:
                self.spritesList_rise_left.append(pygame.transform.flip(sprite, True, False))
        else:
            # Walking
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (1).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (2).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (3).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (4).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (5).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (6).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (7).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (8).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (9).png"), (64, 64)))
            self.spritesList_walk_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/walk/Walk (10).png"), (64, 64)))
            for sprite in self.spritesList_walk_right:
                self.spritesList_walk_left.append(pygame.transform.flip(sprite, True, False))

            # Dying
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (1).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (2).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (3).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (4).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (5).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (6).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (7).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (8).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (9).png"), (64, 64)))
            self.spritesList_die_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (10).png"), (64, 64)))
            for sprite in self.spritesList_die_right:
                self.spritesList_die_left.append(pygame.transform.flip(sprite, True, False))

            # Rising
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (10).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (9).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (8).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (7).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (6).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (5).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (4).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (3).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (2).png"), (64, 64)))
            self.spritesList_rise_right.append(
                pygame.transform.scale(pygame.image.load("images/zombie/girl/dead/Dead (1).png"), (64, 64)))
            for sprite in self.spritesList_rise_right:
                self.spritesList_rise_left.append(pygame.transform.flip(sprite, True, False))

        # Load an image and get rect
        self.direction = random.choice([-1, 1]) #-1 gremlins move left, 1 move right

        self.current_sprite = 0
        if self.direction == -1:
            self.image = self.spritesList_walk_left[self.current_sprite]
        else:
            self.image = self.spritesList_walk_right[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (random.randint(100, WIN_WIDTH - 100), -100) #-100 for y val, gremlins created top of the screen.

        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group

        # Animation booleans
        self.animate_death = False
        self.animate_rise = False

        # Load sounds
        self.hit_sound = pygame.mixer.Sound("sounds/zombie_hit.wav")
        self.kick_sound = pygame.mixer.Sound("sounds/zombie_kick.wav")
        self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")

        # Kinematics vectors
        self.position = vector(self.rect.x, self.rect.y)
        self.velocity = vector(self.direction * random.randint(min_speed, max_speed), 0)
        self.acceleration = vector(0, self.GREMLIN_VERTICAL_ACCELERATION)

        # Intial zombie values
        self.is_dead = False #keeps track if hunter killed the gremlins
        self.round_time = 0 #
        self.frame_count = 0  

    # This updates the aliens
    # This is from the Sprite update method
    def update(self):
        from main import SECONDS
        self.move()
        self.check_aliens_collision()
        self.check_aliens_animation()

        # Determine when teh gremlin should rise from the dead
        if self.is_dead:
            self.frame_count += 1
            if self.frame_count % SECONDS == 0:
                self.round_time += 1
                if self.round_time == self.RISE_TIME:
                    self.animate_rise = True
                    # When the gremlin died, the image was kept as the last image
                    # When it rises, we want to start at index 0 of our rise_sprite lists
                    self.current_sprite = 0

    # to MOve the aliens
    def move(self):
        from main import WIN_WIDTH, WIN_HEIGHT

        # We don't need to update the accelreation vector because it never changes here
        if not self.is_dead:
            if self.direction == -1: # -1 dir is moving to the left
                self.aliens_action_animation(self.spritesList_walk_left, .5)
            else:
                self.aliens_action_animation(self.spritesList_walk_right, .5)

            # Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
            self.velocity += self.acceleration
            self.position += self.velocity + 0.5 * self.acceleration

            # Update rect based on kinematic calculations and add wrap around movement
            if self.position.x < 0:
                self.position.x = WIN_WIDTH
            elif self.position.x > WIN_WIDTH:
                self.position.x = 0

            self.rect.bottomleft = self.position

    # checks collision of the aliens with platforms of the game and portals
    def check_aliens_collision(self):
        from main import WIN_WIDTH, WIN_HEIGHT
        # Collision check between zombie and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0 #stop velocity in y-dir if they fall on the platform

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

    # Checks if the aliens death/re-spawn animation runs
    def check_aliens_animation(self):
        #adding gremlins death animation
        if self.animate_death:
            if self.direction == 1:
                self.aliens_action_animation(self.spritesList_die_right, .095)
            else:
                self.aliens_action_animation(self.spritesList_die_left, .095)

        # Animate the zombie rise
        if self.animate_rise:
            if self.direction == 1:
                self.aliens_action_animation(self.spritesList_rise_right, .095)
            else:
                self.aliens_action_animation(self.spritesList_rise_left, .095)



    # This method animates the aliens actions
    def aliens_action_animation(self, sprite_list, speed ):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            #ending the death animation
            if self.animate_death:
                self.current_sprite = len(sprite_list) - 1 #setting gremlin to the last animation picture
                self.animate_death = False

            # End the rise animation
            if self.animate_rise:
                self.animate_rise = False
                self.is_dead = False #make gremlins alive again
                self.frame_count = 0
                self.round_time = 0

        self.image = sprite_list[int(self.current_sprite)]
