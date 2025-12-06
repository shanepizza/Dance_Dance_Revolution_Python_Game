import pygame
from left_screen import LeftScreen
import get_from_files as gff
from right_screen import RightScreen


pygame.init()  # Initialize once at module level

#The GameWindow is what holds the main loop and handles timing/frame rate
#This is the main window not the game screen itself.
#It draws the GameScreen to the computer screen as the gamescreen updates. 
class GameWindow:
    def __init__(self, width=None, height=None):
        # Use None as defaults, then get values if not provided
        if width is None:
            width = gff.get_window_width()
        if height is None:
            height = gff.get_window_height()
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Dance Dance Revolution")
        self.clock = pygame.time.Clock()
        self.fps = gff.get_refresh_rate()  # 60 from config

        self.running = True

        # Create an instance of GameScreen and RightScreen
        self.left_screen = LeftScreen(width//2, height)
        self.right_screen = RightScreen(self, width//2, height)

    

    #Itterates through all events in the pygame event queue
    def handle_events(self):
        pass
        #or event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        self.running = False
    
    #Any gamewindow updates go here
    def update(self):
        # Update game state here if needed
        self.left_screen.update()
        self.right_screen.update()
            
    
    def draw(self):
        #call the grame screen draw method
        self.left_screen.draw()
        self.right_screen.draw()

        # Draw the GameScreen to the window
        self.window.blit(self.left_screen, (0, 0))
        self.window.blit(self.right_screen, (gff.get_window_width()//2, 0))
        pygame.display.flip()

#this is the main loop for the game window
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)  # GameWindow controls frame rate
        pygame.quit()


if __name__ == "__main__":
    game_window = GameWindow()
    #game_window.left_screen.add_arrow(position=(100, 0), arrow_code=1)
    game_window.run()


