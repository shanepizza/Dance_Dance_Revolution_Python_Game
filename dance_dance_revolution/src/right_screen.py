import pygame
import get_from_files as gff
import custom_button as button
import button_handler as btn_handler

#This is the class the will handle the right side of the screen with the buttons 
class RightScreen(pygame.Surface):
    def __init__(self, parent, width=None, height=None):
        self.parent = parent
        if width is None:
            width = gff.get_window_width()//2
        if height is None:
            height = gff.get_window_height()
        self.background_color = gff.get_right_background_screen_color()
        
        super().__init__((width, height))
        #set possition to right half of the screen
        self.get_rect(topleft=(gff.get_window_width()//2, 0))
        
        #create the button handler
        self.button_handler = btn_handler.ButtonHandler(self)
        #create list of all buttons
        self.buttons = pygame.sprite.Group()
        #list of button image paths and positions
        self.button_list = [
            ("arrow_NW.png", (50, 50), 1),
            ("arrow_N.png", (150, 50), 2),
            ("arrow_NE.png", (250, 50), 3),
            ("arrow_W.png", (50, 150), 4),
            ("arrow_E.png", (250, 150), 5),
            ("arrow_SW.png", (50, 250), 6),
            ("arrow_S.png", (150, 250), 7),
            ("arrow_SE.png", (250, 250), 8)
        ]
        #Call create buttons method
        self.create_all_buttons()
    def change_parent_running(self, value):
        self.parent.running = value

    def add_button(self, path, position):
        new_button = button.CustomButton(path, position)
        self.buttons.add(new_button)

    def create_all_buttons(self):
        for item in self.button_list:
            self.add_button(path=item[0], position=item[1])

#add in a button handler for when each button is pressed.
    def button_handler(self):
        pass




    def draw(self):
        #draw green background
        self.fill(self.background_color)
        # Draw all buttons onto the RightScreen
        for button in self.buttons:
            if hasattr(button, 'shadow_image'):
                self.blit(button.shadow_image, button.shadow_rect)
            self.blit(button.image, button.rect)

    # Update method that calls the button handler
    def update(self):
        self.button_handler.check_events()
        
            
        #This will call the update() for the button handler 
        #self.button_handler.update()




