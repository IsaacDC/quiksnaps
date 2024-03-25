import pygame
import pygame.camera
import sys

if __name__ == "__main__":

    pygame.init()
    display = pygame.display.set_mode((1080,1920), pygame.FULLSCREEN)
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (1280,720))
    cam.start()

    while True:
        img = cam.get_image()
        display.blit(img, (0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cam.stop()
                pygame.quit()
                sys.exit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(cam.get_size())
                    cam.stop()
                    pygame.quit()
                    sys.exit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.image.save(img, "test.png")
                    cam.stop()
                    pygame.quit()
                    sys.exit()
                    
