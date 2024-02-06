from .photoExceptions import nextClassException
import pygame

class step1:

    def __init__(self):
        #self.display = display
        self.count = 0

    def run(self, display = None, events = None):
        '''
        if display == None:
            print("No pygame in step 1")

        if events == None:
            print("No pygame events in step1")
        '''
        for event in events:
            if event.type == pygame.QUIT:
                print("Why stop now?")

        if self.count == 10:
            self.count = 0
            raise nextClassException("Moving on.")

        #print("count is %s"%(self.count))
        self.count = self.count + 1

    def __str__(self):
        return "Step 1"
