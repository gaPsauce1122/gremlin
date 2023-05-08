import pygame

#the diamond is a tile that will be animated and generated through this class.
#This will sit at the top middle of the display
class Diamond_Maker(pygame.sprite.Sprite):
    # initializing diamond maker
    def __init__(self, xcor, ycor, game_main_group):    #add it to main tile group for drawing purposes
        super().__init__()

        # blank list for all the animation we will have. Animation frames
        self.diamond_sprites_animation_frames = []

        #Load all images of diamond. the diamond will rotate. ROTATE ANIMATION for diamond

        # scaling bcoz original diamond picture is 24 x 24 pixels
        self.diamond_sprites_animation_frames.append(pygame.transform.scale(pygame.image.load("images/ruby/tile000.png"), (64,64)))
        self.diamond_sprites_animation_frames.append(pygame.transform.scale(pygame.image.load("images/ruby/tile001.png"), (64,64)))
        self.diamond_sprites_animation_frames.append(pygame.transform.scale(pygame.image.load("images/ruby/tile002.png"), (64,64)))
        self.diamond_sprites_animation_frames.append(pygame.transform.scale(pygame.image.load("images/ruby/tile003.png"), (64,64)))
        self.diamond_sprites_animation_frames.append(pygame.transform.scale(pygame.image.load("images/ruby/tile004.png"), (64,64)))
        self.diamond_sprites_animation_frames.append(pygame.transform.scale(pygame.image.load("images/ruby/tile006.png"), (64,64)))
        self.diamond_sprites_animation_frames.append(pygame.transform.scale(pygame.image.load("images/ruby/tile005.png"), (64,64)))

        #After loading the images. I need to pick one as my starting image.
        #image loaded & get rect
        self.current_diamond_spriteList_index = 0 #this is an index to keep track of self.diamond_sprites_animation_frames = []
        self.image = self.diamond_sprites_animation_frames[self.current_diamond_spriteList_index]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (xcor, ycor)

        # Add to the main game group for drawing purposes on the display
        game_main_group.add(self)

    # This updates the diamond maker
    # This is from the Sprite update method
    def update(self):
        #no one interacts with this diamond. nor hunter nor gremlin
        #only thing is dimaond will update as it will animate everytime I call the game loop
        self.animate_diamond(self.diamond_sprites_animation_frames, 0.25) #4 loops to move to next frame

    # to animate the diamond
    def animate_diamond(self, diamond_sprites_list, animation_speed):
        """Animate the diamond maker"""
        if self.current_diamond_spriteList_index < len(diamond_sprites_list) - 1:
            self.current_diamond_spriteList_index += animation_speed #if index is 0 and speed is 1, next index is 0 +1 = 1
        else:
            self.current_diamond_spriteList_index = 0

        #Adding the items to our self.image and int so that when we put speed 0.5, the list index is an int
        #Setting the images
        self.image = diamond_sprites_list[int(self.current_diamond_spriteList_index)]