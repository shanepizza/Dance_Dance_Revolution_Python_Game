import pygame as pg

class ButtonHandler:
    def __init__(self, parent):
        self.parent = parent
    """
    def check_for_QUIT(self):
        #if event contains QUIT event, return False to the game_window run loop
         
        for event in events:
            if event.type == pg.QUIT:
                self.parent.change_parent_running(False)
    """      
    def check_events(self):
        events = pg.event.get()
        checked_press = self.check_keypress(events)
        self.parent.parent.left_screen.all_sprites.update(checked_press[1] if checked_press else None)
        checked_release = self.check_keyrelease(events)
        

    def check_keypress(self, events=None):
        #If events is empty, end the function
        if events is None:
            return
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg .K_SPACE:
                    print("Space pressed!")
                elif event.key == pg.K_LEFT:
                    print("Left arrow pressed!")
                elif event.key == pg.K_ESCAPE:
                    print("Escape pressed!")
                
                #Check if any of the numpad keys are pressed
                elif event.key == pg.K_KP1:
                    print("Numpad 1 pressed!")
                    #This will call the press action for the button object. 
                    #Then we repeat for all the numpad keys.
                    self.parent.buttons.sprites()[5].press_action()
                    return (True, 1) 
                elif event.key == pg.K_KP2:
                    print("Numpad 2 pressed!")
                    self.parent.buttons.sprites()[6].press_action()
                    return (True, 2) 
                elif event.key == pg.K_KP3:
                    print("Numpad 3 pressed!")
                    self.parent.buttons.sprites()[7].press_action()
                    return (True, 3) 
                elif event.key == pg.K_KP4:
                    print("Numpad 4 pressed!")
                    self.parent.buttons.sprites()[3].press_action()
                    return (True, 4)
                #elif event.key == pg.K_KP5:
                  #  print("Numpad 5 pressed!")
                elif event.key == pg.K_KP6:
                    print("Numpad 6 pressed!")
                    self.parent.buttons.sprites()[4].press_action()
                    return (True, 5)
                elif event.key == pg.K_KP7:
                    print("Numpad 7 pressed!")
                    self.parent.buttons.sprites()[0].press_action()
                    return (True, 6)
                elif event.key == pg.K_KP8:
                    print("Numpad 8 pressed!")
                    self.parent.buttons.sprites()[1].press_action()
                    return (True, 7)
                elif event.key == pg.K_KP9:
                    print("Numpad 9 pressed!")
                    self.parent.buttons.sprites()[2].press_action()
                    return (True, 8)
            if event.type == pg.QUIT:
                print("Quit event detected.")
                self.parent.parent.running = False

    def check_keyrelease(self, events=None):
        #If events is empty, end the function
        if events is None:
            return
    
        for event in events:
            if event.type == pg.KEYUP:
                if event.key == pg.K_KP1:
                    print("Numpad 1 released!")
                    self.parent.buttons.sprites()[5].release_action()
                    return (True, 5) 
                elif event.key == pg.K_KP2:
                    print("Numpad 2 released!")
                    self.parent.buttons.sprites()[6].release_action()
                    return (True, 6) 
                elif event.key == pg.K_KP3:
                    print("Numpad 3 released!")
                    self.parent.buttons.sprites()[7].release_action()
                    return (True, 7) 
                elif event.key == pg.K_KP4:
                    print("Numpad 4 released!")
                    self.parent.buttons.sprites()[3].release_action()
                    return (True, 3)
                #elif event.key == pg.K_KP5:
                  #  print("Numpad 5 released!")
                elif event.key == pg.K_KP6:
                    print("Numpad 6 released!")
                    self.parent.buttons.sprites()[4].release_action()
                    return (True, 4)
                elif event.key == pg.K_KP7:
                    print("Numpad 7 released!")
                    self.parent.buttons.sprites()[0].release_action()
                    return (True, 0)
                elif event.key == pg.K_KP8:
                    print("Numpad 8 released!")
                    self.parent.buttons.sprites()[1].release_action()
                    return (True, 1)
                elif event.key == pg.K_KP9:
                    print("Numpad 9 released!")
                    self.parent.buttons.sprites()[2].release_action()
                    return (True, 2)
        