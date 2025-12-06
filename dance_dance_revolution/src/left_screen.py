import pygame
import random
import get_from_files as gff
import ArrowSprite as arrow

#The GameScreen is what we use to handle all sprite updates and maybe game logic? 
#once the GameScreen has updated everything, the GameWindow just draws it to the computer screen.
class LeftScreen(pygame.Surface):
    def __init__(self, width=None, height=None):
        if width is None:
            width = gff.get_window_width()//2
        if height is None:
            height = gff.get_window_height()
        self.background_color = gff.get_left_background_screen_color()
        
        super().__init__((width, height))
        self.all_sprites = pygame.sprite.Group()
        self.count_down = 60
    arrow_hash_table = {
        1: "arrow_SW.png",
        2: "arrow_S.png",
        3: "arrow_SE.png",
        4: "arrow_W.png",
        5: "arrow_E.png",
        6: "arrow_NW.png",
        7: "arrow_N.png",
        8: "arrow_NE.png"
    }

    #add arrow method. call to create a new arrow sprite and add it to the group
    def add_arrow(self, position, arrow_code=1):
        #determine image path based on arrow type
        #use a switch case for this
        image_name = self.arrow_hash_table.get(arrow_code)
        new_arrow = arrow.ArrowSprite(image_name, position, arrow_code)
        self.all_sprites.add(new_arrow)




    def remove_off_screen_arrows(self):
        screen_height = gff.get_window_height()
        for sprite in self.all_sprites:
            if isinstance(sprite, arrow.ArrowSprite) and sprite.is_off_screen(screen_height):
                self.all_sprites.remove(sprite)

    def count_down_tick(self):
        self.count_down -= 1
        if self.count_down <= 0:
            self.count_down = 60
            self.add_arrow(position=(100, 0), arrow_code=random.randint(1, 8))

    def set_bottom_arrow(self):
        #This checks the y positions of all arrows and changes the is_bottom_arrow boolean 
        # value at the lowest y position to true
        
        if self.all_sprites:
            max(self.all_sprites, key=lambda sprite: sprite.rect.y).set_bottom_arrow(True)
        


    def update(self):
        # Update all sprites in the GameScreen
        self.all_sprites.update()
        self.remove_off_screen_arrows()
        self.set_bottom_arrow()
        self.count_down_tick()


    
    def draw(self):

        #draw red background
        self.fill(self.background_color)

        # Draw all sprites onto the GameScreen
        self.all_sprites.draw(self)
