import pygame
from photoplugins.photoExceptions import nextClassException

class photoManager:
    _instance = None


    def __new__(self):
        if self._instance is None:
            self._instance  = super(photoManager, self).__new__(self)
            self._instance.classes = []
            pygame.init()
            self._instance.display = pygame.display.set_mode((1080,1920), pygame.FULLSCREEN)

        return self._instance


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
