import pygame as pgame
import get_from_files as gff

#create a custom button class that uses an image for the button
class CustomButton(pgame.sprite.Sprite):
    def __init__(self, image_path, position, btn_code=None):
        self.btn_code = btn_code
        image_path = gff.get_images_path() / image_path
        super().__init__()
        self.image = pgame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        #reshapre to be normal size
        pixel_size = gff.get_button_pixel_size()
        self.image = pgame.transform.scale(self.image, (pixel_size, pixel_size))

        #create second image under the button to make the button look 3D
        self.shadow_image = pgame.Surface((pixel_size, pixel_size))
        self.shadow_image.fill((50, 50, 50))  # Dark gray shadow
        self.shadow_rect = self.shadow_image.get_rect(topleft=(position[0]+5, position[1]+5))

    #is_pressed method that is meant to be called by the button hanlder
    def is_pressed(self):
        #move the button down by 5 pixels to simulate being pressed
        self.rect.y += 3
        self.rect.x += 5
        
    
    def is_released(self):
        #move the button back to original position
        self.rect.y -= 3
        self.rect.x -= 5

    def press_action(self):
        #When this is called, move the button down and back up
        #move image down
        self.is_pressed()
        #redraw the screen to show the button pressed
        
    def release_action(self):    
        #move image back up
        self.is_released()
        
        #button handler will be a module that handles all keys that can be pressed.
        #I suppose this will be a singleton class?
        
        #The check_keypress method will return a tuple of (True/False, key_code)
        #It will return a tuple of a boolean for the button class to check and 
        #a code for the game screen to handle the action logic.
        #check if the keyboard key is pressed

        
        
        
        
        
    