from .photoExceptions import nextClassException
import pygame

class step1:

    def __init__(self):
        #self.display = display
        self.count = 0

    def run(self, display = None, events = None):

        if display == None:
            print("No pygame in step 2")
            pygame.quit()

        img = pygame.image.load("images/idle.png").convert()
        display.blit(img, (0,0))
        pygame.display.flip()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Next!")
                raise nextClassException("Moving on from Step 1.")

    def __str__(self):
        return "Step 1"
