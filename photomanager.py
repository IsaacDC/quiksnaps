import pygame
from photoplugins.photoExceptions import nextClassException

class photoManager:

    def __init__(self):
        self.classes = []
        self.count = 0
        pygame.init()
        self.display = pygame.display.set_mode((1080,1920), pygame.FULLSCREEN)

    def run(self):
        aClass  = self.classes[0]
        print("Running %s"%(aClass))

        try:
            aClass.run(self.display, pygame.event.get())
        #make an expection class just for this
        except nextClassException:
            aClass = self.classes.pop(0)
            self.classes.append(aClass)


    def register(self, aClass):
        #print(aClass)
        self.classes.append(aClass)
