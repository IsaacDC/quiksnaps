from .photoExceptions import nextClassException
import pygame
import pygame.camera
import sys

class previewCamera:

    def __init__(self):
        self.count = 0
        pygame.camera.init()
        self.cam = pygame.camera.Camera("/dev/video0")
        self.cam.start()

    def run(self, display = None, events = None):

        if display == None:
            print("No pygame in step 2")
            pygame.quit()

        top = pygame.image.load("images/top.png").convert()
        bottom = pygame.image.load("images/bottom.png").convert()
        camimg = self.cam.get_image()

        display.blit(top, (0,0))
        display.blit(bottom, (0,1704))
        camimg = pygame.transform.scale_by(camimg, 1.5)
        display.blit(camimg, (70,600))
        pygame.display.flip()

        for event in events:
            if event.type == pygame.QUIT:
                self.cam.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.cam.stop()
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Next!")
                display.fill((0,0,0))
                pygame.display.flip()
                pygame.event.clear()
                

                raise nextClassException("Moving on from preview.")

    def __str__(self):
        return "Camera preview step"
