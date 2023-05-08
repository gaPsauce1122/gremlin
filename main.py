import pygame
import random
from TileMapping import TileMapping
from Diamond_Maker import Diamond_Maker
from Game_portals import Game_portals
from Hunter import Hunter
from Alien import Alien
from Diamond import Diamond

#Initializing variable for using 2D vectors
vector = pygame.math.Vector2

#Initializing pygame
pygame.init()


#window display is being set
#tile size is 32 x 32
#1280/32 = 40 tiles wide
#736/32 = 21 tiles high
WIN_WIDTH = 1280
WIN_HEIGHT = 672
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Gremlin Knight")

#Setting seconds and clock
SECONDS = 60    #Frames per second
clock = pygame.time.Clock()


#------------------------- Game Controller.py ---------------------------------------
class GameController():

    # Game is initialized
    def __init__(self, hunter, gremlin_group, platform_group, portal_group, bullet_group, diamond_group):

        # Set constant variables
        self.GAME_LEVEL_STARTING_TIME = 30  # 30 secs
        self.STARTING_GREMLIN_CREATION_TIME = 5

        # Setting values for the game
        self.game_score = 0
        self.gameLevel_number = 1
        self.count_frame_nums = 0
        # Timer countdown that shows how  much time left on the screen
        self.gameLevel_time = self.GAME_LEVEL_STARTING_TIME  # this variable decreases GAME_LEVEL_STARTING_TIME by 1
        self.gremlin_appearance_time = self.STARTING_GREMLIN_CREATION_TIME

        # Setting up the game fonts
        self.font_Game_Title = pygame.font.Font("fonts/Poultrygeist.ttf", 48)
        self.font_Game_display = pygame.font.Font("fonts/Pixel.ttf", 24)

        # set sounds
        self.lost_diamond_sound = pygame.mixer.Sound("sounds/lost_ruby.wav")
        self.diamond_collect_sound = pygame.mixer.Sound("sounds/ruby_pickup.wav")
        pygame.mixer.music.load("sounds/level_music.wav")  # opengameart

        # Attaching groups
        self.hunter = hunter
        self.gremlin_group = gremlin_group
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group
        self.diamond_group = diamond_group

    # This method updates the game
    def update(self):
        # Every second, decrease game level time by 1
        self.count_frame_nums += 1
        # self.gameLevel_time -= 1, if i do this the program decreases 60 times every second

        if self.count_frame_nums % SECONDS == 0:  # if frame count divisible by seconds, then we know 1 sec has passed
            self.gameLevel_time -= 1
            self.count_frame_nums = 0

        # Check for gameplay collisions
        self.gameClass_collision_check()
        self.add_gremlins()
        self.check_Level_completion()
        self.game_end_check()

    # This draws the game display
    def draw(self):
        # declaring color constants
        WHITE = (255, 255, 255)
        GREEN = (25, 200, 25)

        # Setting up the texts on the game display
        text_score = self.font_Game_display.render("Score: " + str(self.game_score), True, WHITE)
        score_text_rect = text_score.get_rect()
        score_text_rect.topleft = (10, WIN_HEIGHT - 50)  # bottom of the Window on the dirt tile

        text_hunter_health = self.font_Game_display.render("Health: " + str(self.hunter.hunter_health), True, WHITE)
        text_health_rect = text_hunter_health.get_rect()
        text_health_rect.topleft = (10, WIN_HEIGHT - 25)  # Right below our score text

        game_Title_text = self.font_Game_Title.render("Gremlin Knight", True, GREEN)
        text_title_rect = game_Title_text.get_rect()
        text_title_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT - 25)  # Center horizontally. middle of the screen

        level_num_text = self.font_Game_display.render("Night: " + str(self.gameLevel_number), True, WHITE)
        level_num_rect = level_num_text.get_rect()
        level_num_rect.topright = (WIN_WIDTH - 10, WIN_HEIGHT - 50)  # right side of the display

        gameTime_left_text = self.font_Game_display.render("Sunrise In: " + str(self.gameLevel_time), True, WHITE)
        gameTime_left_text_rect = gameTime_left_text.get_rect()
        gameTime_left_text_rect.topright = (WIN_WIDTH - 10, WIN_HEIGHT - 25)

        # Drawing the game display
        # blitting the fonts to the screen
        display_surface.blit(text_score, score_text_rect)
        display_surface.blit(text_hunter_health, text_health_rect)
        display_surface.blit(game_Title_text, text_title_rect)
        display_surface.blit(level_num_text, level_num_rect)
        display_surface.blit(gameTime_left_text, gameTime_left_text_rect)

    # Method to add gremlins to the game
    def add_gremlins(self):
        # Check to add a gremlin every second
        # 1st- check if single sec has passed
        # 2nd - check current val of our round time, to see if its divisible by gremlin_creation_time
        if self.count_frame_nums % SECONDS == 0:  # =0 means a sec has passed
            # Only add a zombie if zombie creation time has passed
            if self.gameLevel_time % self.gremlin_appearance_time == 0:
                gremlin = Alien(self.platform_group, self.portal_group, self.gameLevel_number, 5 + self.gameLevel_number)
                self.gremlin_group.add(gremlin)

    # Method to check collisions in the game
    def gameClass_collision_check(self):
        # See if any bullet in the bullet group hit a zombie in the zombie group
        # in this dict key is bullet and values is gremlins
        collision_dict = pygame.sprite.groupcollide(self.bullet_group, self.gremlin_group, True,
                                                    False)  # destroy bullet not gremlin
        if collision_dict:
            for gremlins in collision_dict.values():
                for gremlin in gremlins:
                    gremlin.hit_sound.play()
                    gremlin.is_dead = True
                    gremlin.animate_death = True

        # See if a player stomped a dead zombie to finish it or collided with a live zombie to take damage
        collision_list = pygame.sprite.spritecollide(self.hunter, self.gremlin_group, False)
        if collision_list:
            for gremlin1 in collision_list:
                # The zombie is dead; stomp it
                if gremlin1.is_dead == True:
                    gremlin1.kick_sound.play()
                    gremlin1.kill()  # removes the gremlin from the game/list
                    self.game_score += 25

                    diamond = Diamond(self.platform_group, self.portal_group)
                    self.diamond_group.add(diamond)

                # The zombie isn't dead, so take damage
                else:
                    self.hunter.hunter_health -= 20
                    self.hunter.hunter_hit_audio.play()
                    # move the hunter to not continually take the damage
                    self.hunter.hunter_position.x -= 256 * gremlin1.direction
                    self.hunter.rect.bottomleft = self.hunter.hunter_position

        # See if a player collided with a diamond
        if pygame.sprite.spritecollide(self.hunter, self.diamond_group, True):  # true means collided with a diamond
            self.diamond_collect_sound.play()
            self.game_score += 100
            self.hunter.hunter_health += 10
            if self.hunter.hunter_health > self.hunter.BEGINNING_HEALTH:  # capping the hunter health. just say health = 95 and we add 10, we do not want health to be 105
                self.hunter.hunter_health = self.hunter.BEGINNING_HEALTH

        # See if a living gremlin collided with a diamond
        for gremlin in self.gremlin_group:
            if gremlin.is_dead == False:
                if pygame.sprite.spritecollide(gremlin, self.diamond_group, True):  # true is destroy diamond
                    self.lost_diamond_sound.play()
                    gremlin = Alien(self.platform_group, self.portal_group, self.gameLevel_number,
                                    5 + self.gameLevel_number)  # new gremlin created when a living gremlin collides with a diamond
                    self.gremlin_group.add(gremlin)

    # Checks if a level has been completed and the hunter survives the night
    # If the time is 0, so the hunter is alive and survived the night
    def check_Level_completion(self):
        if self.gameLevel_time == 0:
            self.start_new_night()

    # Method for Game Over and checks if the player lost the game
    def game_end_check(self):
        if self.hunter.hunter_health <= 0:
            pygame.mixer.music.stop()
            self.game_pause("Game Over! Final Score: " + str(self.game_score), "Press 'Enter' to play again...")
            self.game_reset()

    # To start a new night/round method
    def start_new_night(self):
        self.gameLevel_number += 1

        # Decrease zombie creation time...more zombies
        if self.gameLevel_number < self.STARTING_GREMLIN_CREATION_TIME:  # no negative gremlin creation time
            self.gremlin_appearance_time -= 1

        # Reset round values
        self.gameLevel_time = self.GAME_LEVEL_STARTING_TIME

        self.gremlin_group.empty()
        self.diamond_group.empty()
        self.bullet_group.empty()

        self.hunter.hunter_position_reset()
        self.game_pause("You survived the night!", "Press 'Enter' to continue...")

    # to pause the game
    def game_pause(self, main_text, sub_text):
        global gameOn

        pygame.mixer.music.pause()

        # Set colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREEN = (25, 200, 25)

        # Create main pause text
        main_text = self.font_Game_Title.render(main_text, True, GREEN)
        main_rect = main_text.get_rect()
        main_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)  # middle of the screen

        # Create sub pause text
        sub_text = self.font_Game_Title.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 64)

        # Display the pause text
        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        # Pause the game until user hits enter or quits
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # User wants to continue
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                        pygame.mixer.music.unpause()
                # User wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    gameOn = False
                    pygame.mixer.music.stop()

    # reset the game
    def game_reset(self):
        # Reset game values
        self.game_score = 0
        self.gameLevel_number = 1
        self.gameLevel_time = self.GAME_LEVEL_STARTING_TIME
        self.gremlin_appearance_time= self.STARTING_GREMLIN_CREATION_TIME

        # Reset the player
        self.hunter.hunter_health = self.hunter.BEGINNING_HEALTH
        self.hunter.hunter_position_reset()

        # Empty sprite groups
        self.gremlin_group.empty()
        self.diamond_group.empty()
        self.bullet_group.empty()

        pygame.mixer.music.play(-1, 0.0)
#--------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

#Create the tile map
#0 -> no tile, 1 -> dirt, 2-5 -> platforms, 6 -> diamond maker, 7-8 -> portals, 9 -> player
#21 rows and 40 columns
game_tile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#Creating groups
game_tile_group = pygame.sprite.Group()
game_platform_group = pygame.sprite.Group()

hunter_group = pygame.sprite.Group()
bullet_fired_group = pygame.sprite.Group()

gremlins_group = pygame.sprite.Group()

game_portal_group = pygame.sprite.Group()

diamond_group = pygame.sprite.Group()
#diamond maker will be added to the game tile group. it is just a class with some animation funtions
#so doesnot need a group

#making Tile objects from the game_tile_map
#Looping thrpugh the 21 lists (rows) in the tile map(r moves us down the map)
for r in range(len(game_tile_map)):
    # Loop through the 40 elements in a given list (cols) (c moves us across the map)
    for c in range(len(game_tile_map[r])):
        # Dirt tiles
        if game_tile_map[r][c] == 1:
            TileMapping(c * 32, r * 32, 1, game_tile_group)  #1 is an image int. for y-val is r as it moves us down the map
            #Platform tiles
        elif game_tile_map[r][c] == 2:
            TileMapping(c * 32, r * 32, 2, game_tile_group, game_platform_group)
        elif game_tile_map[r][c] == 3:
            TileMapping(c * 32, r * 32, 3, game_tile_group, game_platform_group)
        elif game_tile_map[r][c] == 4:
            TileMapping(c * 32, r * 32, 3, game_tile_group, game_platform_group)
        elif game_tile_map[r][c] == 5:
            TileMapping(c * 32, r * 32, 5, game_tile_group, game_platform_group)
        #Diamond maker
        elif game_tile_map[r][c] == 6:
            Diamond_Maker(c * 32, r * 32, game_tile_group)
        #Portals
        elif game_tile_map[r][c] == 7:
            Game_portals(c * 32, r * 32, "green", game_portal_group)
        elif game_tile_map[r][c] == 8:
            Game_portals(c * 32, r * 32, "purple", game_portal_group)
        #Our Hunter
        elif game_tile_map[r][c] == 9:
            hunter_obj = Hunter(c * 32 - 32, r * 32 + 32, game_platform_group, game_portal_group, bullet_fired_group) #ddd 32 to push it down
            hunter_group.add(hunter_obj)


#Loading a background image
background_pic = pygame.transform.scale(pygame.image.load("images/background.png"), (1280, 736))
background_rect = background_pic.get_rect()
background_rect.topleft = (0, 0)

#Now i create a gameController object
game_control = GameController(hunter_obj, gremlins_group, game_platform_group, game_portal_group, bullet_fired_group, diamond_group)
game_control.game_pause("Gremlin Knight", "Press 'Enter' to Begin")
pygame.mixer.music.play(-1, 0.0)


#--------------GAME LOOP-------------------------
gameOn = True
while gameOn:
    #checking if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if event.type == pygame.KEYDOWN:
            #Hunter wants to jump
            if event.key == pygame.K_SPACE:
                hunter_obj.hunter_jump()
            #Hunter wants to fire
            if event.key == pygame.K_UP:
                hunter_obj.hunter_fires()

    #background blit
    display_surface.blit(background_pic, background_rect)

    #tile is drawn here and diamond maker is updates
    game_tile_group.update()
    game_tile_group.draw(display_surface)

    #Drawing and updating portal groups
    game_portal_group.update()
    game_portal_group.draw(display_surface)

    #Draw hunter group and update
    hunter_group.update()
    hunter_group.draw(display_surface)

    #Updating the game and drawing
    game_control.update()
    game_control.draw()

    #Updating the bullet group and drawing it
    bullet_fired_group.update()
    bullet_fired_group.draw(display_surface)

    gremlins_group.update()
    gremlins_group.draw(display_surface)

    diamond_group.update()
    diamond_group.draw(display_surface)


    # This will update the display window and tick the clock
    pygame.display.update()
    clock.tick(SECONDS)

# The game ends
pygame.quit()



