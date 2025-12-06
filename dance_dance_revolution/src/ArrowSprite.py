#Sprite class for arrows that fall down the screen in DDR game
import get_from_files as gff
import pygame as pg

class ArrowSprite(pg.sprite.Sprite):
    def __init__(self, image_name, position, arrow_code):
        super().__init__()
        self.image = pg.image.load(gff.get_images_path() / image_name).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.speed = gff.get_arrow_speed()  # Speed at which the arrow falls
        #Adjust the arrow size to be pixel size set in config
        pixel_size = gff.get_arrow_pixel_size()
        #Scale the image to the desired pixel size
        self.image = pg.transform.scale(self.image, (pixel_size, pixel_size))
        #Key code associated with this arrow
        self.arrow_code = arrow_code  
        #Flag to indicate if arrow is the bottom most arrow
        self.is_bottom_arrow = False  
        
        
    
    def check_arrow_code_for_kill(self, key_code=0):
        if self.arrow_code == key_code and self.is_bottom_arrow:
            self.kill()

    def set_bottom_arrow(self, is_bottom):
        self.is_bottom_arrow = is_bottom

    def update(self, *args):
        self.rect.y += self.speed  # Move the arrow down the screen
        self.check_arrow_code_for_kill(args[0] if args else None)

    def is_off_screen(self, screen_height):
        return self.rect.top > screen_height
    
    
        
        #placeholder for future use
        pass