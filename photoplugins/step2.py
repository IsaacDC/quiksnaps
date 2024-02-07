from .photoExceptions import nextClassException
import pygame
import time


class step2:

    def __init__(self):
        #self.display = display
        self.count = 0

    def run(self, display = None, events = None):

        if display == None:
            print("No pygame in step 2")
            pygame.quit()
        
        display.fill((255,255,255))
        print("Step 2")
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        pygame.display.update()
        time.sleep(1)
        raise nextClassException("Moving on from Step 2.")

    def __str__(self):
        return "Step 2"
