import pygame


if __name__ == "__main__":

    pygame.init()
    display = pygame.display.set_mode((1080,1920), pygame.FULLSCREEN)
    cam = pygame.camera.Camera(0)
    cam.start()

    while True:

        for event in events:
            if event.type == pygame.QUIT:
                cam.stop()
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(cam.get_size())
                    cam.stop()
                    pygame.quit()
                    return
        img = cam.get_image()
        display.blit(img, (0,0))
        pygame.display.flip()
