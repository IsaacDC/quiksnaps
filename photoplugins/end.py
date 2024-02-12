from .photoExceptions import nextClassException
import pygame
import time

class laststep:

    def __init__(self):
        #self.display = display
        self.count = 0
        self.fontObj = pygame.font.Font('fonts/segoe-ui.ttf', 16)

    def run(self, display = None, events = None):

        if display == None:
            print("No pygame in laststep")
            pygame.quit()

        img = pygame.image.load("images/end.png").convert()
        display.blit(img, (0,0))
        pygame.display.flip()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        time.sleep(10)
        raise nextClassException("Moving on from Step 1.")

    def __str__(self):
        return "Step 1"
