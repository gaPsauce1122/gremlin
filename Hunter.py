#This class will inherit from sprite class
#This class is the hunter that the user controls
import pygame.sprite
import pygame


#Initializing variable for using 2D vectors
vector = pygame.math.Vector2

#window display is being set
WIN_WIDTH = 1280
WIN_HEIGHT = 672

class Hunter(pygame.sprite.Sprite):
    def __init__(self, xcor, ycor, g_platform, g_portal, bullet_group):
        """Initialize the player"""
        super().__init__()

        #Declaring constant variables that will eventually affect the gameplay of the Hunter
        self.ACCELERATION_HORIZONTAL = 2 #how fast hunter moves when we press a key
        self.FRICTION_HORIZONTAL = 0.15 #SLIPPERY slide motion
        self.ACCELERATION_VERTICAL = 0.8  # serves as Gravity. when we move off of a plaform, we gonna move, fall and accelarate under force of gravity
        self.SPEED_JUMPING_VERTICAL = 18  # Determines how high the Hunter can jump
        self.BEGINNING_HEALTH = 100
        '''Speed is the time rate at which an object is moving along a path,
           while velocity is the rate and direction of an object's movement.'''

        # Empty sprite lists to hold Animation frames for Hunter movements
        self.spritesList_move_right = []
        self.spritesList_move_left = []
        self.spritesList_idle_right = []
        self.spritesList_idle_left = []
        self.spritesList_jump_right = []
        self.spritesList_jump_left = []
        self.spritesList_attack_right = []
        self.spritesList_attack_left = []

        #Now uploading the moving animation images to the game display
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (1).png"), (64, 64))) #original img too big 508 pixels
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (2).png"), (64, 64)))
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (3).png"), (64, 64)))
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (4).png"), (64, 64)))
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (5).png"), (64, 64)))
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (6).png"), (64, 64)))
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (7).png"), (64, 64)))
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (8).png"), (64, 64)))
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (9).png"), (64, 64)))
        self.spritesList_move_right.append(
            pygame.transform.scale(pygame.image.load("images/player/run/Run (10).png"), (64, 64)))
        for sprite in self.spritesList_move_right:
            self.spritesList_move_left.append(pygame.transform.flip(sprite, True, False))

        # #Idle images loaded for the game display
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (1).png"), (64, 64)))
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (2).png"), (64, 64)))
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (3).png"), (64, 64)))
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (4).png"), (64, 64)))
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (5).png"), (64, 64)))
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (6).png"), (64, 64)))
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (7).png"), (64, 64)))
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (8).png"), (64, 64)))
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (9).png"), (64, 64)))
        self.spritesList_idle_right.append(
            pygame.transform.scale(pygame.image.load("images/player/idle/Idle (10).png"), (64, 64)))
        for sprite in self.spritesList_idle_right:
            self.spritesList_idle_left.append(pygame.transform.flip(sprite, True, False))

        # Jump animation images loaded
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (1).png"), (64, 64)))
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (2).png"), (64, 64)))
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (3).png"), (64, 64)))
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (4).png"), (64, 64)))
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (5).png"), (64, 64)))
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (6).png"), (64, 64)))
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (7).png"), (64, 64)))
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (8).png"), (64, 64)))
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (9).png"), (64, 64)))
        self.spritesList_jump_right.append(
            pygame.transform.scale(pygame.image.load("images/player/jump/Jump (10).png"), (64, 64)))
        for sprite in self.spritesList_jump_right:
            self.spritesList_jump_left.append(pygame.transform.flip(sprite, True, False))

        # Attack animation image loaded
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (1).png"), (64, 64)))
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (2).png"), (64, 64)))
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (3).png"), (64, 64)))
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (4).png"), (64, 64)))
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (5).png"), (64, 64)))
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (6).png"), (64, 64)))
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (7).png"), (64, 64)))
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (8).png"), (64, 64)))
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (9).png"), (64, 64)))
        self.spritesList_attack_right.append(
            pygame.transform.scale(pygame.image.load("images/player/attack/Attack (10).png"), (64, 64)))
        for sprite in self.spritesList_attack_right:
            self.spritesList_attack_left.append(pygame.transform.flip(sprite, True, False))

        # Load image and get rect
        self.current_sprite = 0
        self.image = self.spritesList_idle_right[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (xcor, ycor)

        # #Attaching the sprite groups to hunter objects
        self.g_platform = g_platform
        self.g_portal = g_portal
        self.bullet_group = bullet_group

        #idle is fine. when hunter not moving
        #move is pressing a key to move right or left
        #for attack/jump, when I press a key the animation should work even when i am not pressing the key
        #declaring Booleans to check this animation working
        self.jumping_animation = False
        self.shooting_animation = False

        #Sounds associated with the hunter
        #Sounds loaded
        self.jumping_audio = pygame.mixer.Sound("sounds/jump_sound.wav")
        self.attack_audio = pygame.mixer.Sound("sounds/slash_sound.wav")
        self.collide_portal_audio = pygame.mixer.Sound("sounds/portal_sound.wav")
        self.hunter_hit_audio = pygame.mixer.Sound("sounds/player_hit.wav")

        #To help us with motion, declaring Kinematics vectors
        #Kinematics is the study of motion of a system of bodies
        #without directly considering the forces or potential fields affecting the motion.
        self.hunter_position = vector(xcor, ycor)
        self.hunter_velocity = vector(0, 0)
        # in x direction i dont wanna accelerate unless press a key
        #in y dir, i want vertical acceleration be due to gravity
        self.hunter_acceleration = vector(0, self.ACCELERATION_VERTICAL)

        # Set intial player values
        self.hunter_health = self.BEGINNING_HEALTH
        self.starting_xcor = xcor
        self.starting_ycor = ycor

    def update(self):
        """Update the player"""
        self.move()
        self.check_hunter_collisions()
        self.check_hunter_animations()

        # Update the hunter mask
        self.mask = pygame.mask.from_surface(self.image)


    def move(self):
        #The acceleration vector is set
        #acceleration will trigger the movements
        # 0 bcoz initially hunter dont move unless a key is pressed
        # vertical_acc to be present in Y direction due to gravity
        self.hunter_acceleration = vector(0, self.ACCELERATION_VERTICAL)

        #Now check if User pressing a key, the x-component of the acceleration to be non-Zero
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.hunter_acceleration.x = -1 * self.ACCELERATION_HORIZONTAL #.x -> as we changing x-component, -1 bcoz moving left
            self.hunter_action_animation(self.spritesList_move_left, 0.5)
        elif keys[pygame.K_RIGHT]:
            self.hunter_acceleration.x = self.ACCELERATION_HORIZONTAL
            self.hunter_action_animation(self.spritesList_move_right, 0.5)
        else:
            if self.hunter_velocity.x > 0:
                self.hunter_action_animation(self.spritesList_idle_right, .5)   # velocity > 0 i'm facing right
            else:
                self.hunter_action_animation(self.spritesList_idle_left, .5)


        # Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9) based on the updated acceleration
        self.hunter_acceleration.x -= self.hunter_velocity.x * self.FRICTION_HORIZONTAL #more friction, faster we go. thats multiplying by x-cor of our velocity

        self.hunter_velocity += self.hunter_acceleration
        self.hunter_position += self.hunter_velocity + (0.5*self.hunter_acceleration)

        # Update rect based on kinematic calculations and add wrap around movement
        # so we run off the right, we come over on the left
        if self.hunter_position.x < 0: #we crossed left side of the screen, should come out of the right side of the screen
            self.hunter_position.x = WIN_WIDTH
        elif self.hunter_position.x > WIN_WIDTH:
            self.hunter_position.x = 0

        self.rect.bottomleft = self.hunter_position


    def check_hunter_collisions(self):
        """Check for collisions with platforms and portals"""

        # Collision check between player and platforms when falling
        if self.hunter_velocity.y > 0:       # >0 we moving down
            #we can collide with lot of platforms, so putting all platforms collided with in a list
            collided_platforms = pygame.sprite.spritecollide(self, self.g_platform, False, pygame.sprite.collide_mask)
            if collided_platforms:
                self.hunter_position.y = collided_platforms[0].rect.top + 5
                self.hunter_velocity.y = 0 #ensures we stop moving down

        # Collision check between player and platform if jumping up
        if self.hunter_velocity.y < 0:        #>0 we moving up
            collided_platforms = pygame.sprite.spritecollide(self, self.g_platform, False, pygame.sprite.collide_mask)
            if collided_platforms:
                self.hunter_velocity.y = 0 #do not move up
                #if velocity slow, hunter may land on platform
                #if velocity fast, hunter could be inside the platform
                while pygame.sprite.spritecollide(self, self.g_platform, False):
                    self.hunter_position.y += 1    #pushed hunter down until there is no contact between hunter and paltform
                    self.rect.bottomleft = self.hunter_position

        # Collision check for portals
        if pygame.sprite.spritecollide(self, self.g_portal, False):
            self.collide_portal_audio.play()
            # Determine which portal hunter is moving to
            # Left and right
            if self.hunter_position.x > WIN_WIDTH // 2:  # > means hunter on right, will come out of left
                self.hunter_position.x = 86 # 0 puts in a loop
            else:   #else Hunter on left side, will come out of right
                self.hunter_position.x = WIN_WIDTH - 150

            # Top and bottom
            if self.hunter_position.y > WIN_HEIGHT // 2:   # > means we are bottom of the screen, hunter will be warped bottom of the screen
                self.hunter_position.y = 64
            else:
                self.hunter_position.y = WIN_HEIGHT - 132

            self.rect.bottomleft = self.hunter_position


    #Checks if the Hunter's jump/fire animation works
    def check_hunter_animations(self):
        #hunter's jump is animated
        if self.jumping_animation:
            if self.hunter_velocity.x > 0:
                self.hunter_action_animation(self.spritesList_jump_right, .1)
            else:
                self.hunter_action_animation(self.spritesList_jump_left, .1)

        #Animate the player attack
        if self.shooting_animation:
            if self.hunter_velocity.x > 0:
                self.hunter_action_animation(self.spritesList_attack_right, .25)
            else:
                self.hunter_action_animation(self.spritesList_attack_left, .25)

    #Hunter jumps upward if on a platform
    def hunter_jump(self):
        # Only jump if on a platform
        if pygame.sprite.spritecollide(self, self.g_platform, False):
            self.jumping_audio.play()
            # -1 because hunter moves up
            self.hunter_velocity.y = -1 * self.SPEED_JUMPING_VERTICAL   #this launches the hunter in the air
            self.jumping_animation = True

    #fires Bullet from a sword
    def hunter_fires(self):
        from Bullet_Animate import Bullet_Animate

        self.attack_audio.play()
        Bullet_Animate(self.rect.centerx, self.rect.centery, self.bullet_group, self)
        self.shooting_animation = True

    #This method resets the hunter's position
    def hunter_position_reset(self):
        self.hunter_velocity = vector(0, 0)  # hunter do not move when we reset the hunter.
        self.hunter_position = vector(self.starting_xcor, self.starting_ycor)
        self.rect.bottomleft = self.hunter_position

    #This method animates the HUnter's actions
    def hunter_action_animation(self, sprite_list, hunter_speed):
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += hunter_speed
        else:
            self.current_sprite = 0
            #this ends the endless jump animation ends
            if self.jumping_animation:
                self.jumping_animation = False
            #End the attack animation
            if self.shooting_animation:
                self.shooting_animation = False

        self.image = sprite_list[int(self.current_sprite)]
