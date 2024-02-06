from .photoExceptions import nextClassException
import pygame

class step2:

    def __init__(self):
        #self.display = display
        self.count = 0

    def run(self, display = None, events = None):

        if display == None:
            print("No pygame in step 2")
            pygame.quit()
        '''
        if events == None:
            print("No pygame events in step1")
        '''
        display.fill((255,255,255))
        print("Step 2")
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

    def __str__(self):
        return "Step 2"
