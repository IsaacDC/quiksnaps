from .photoExceptions import nextClassException
import pygame
import pygame.camera
import sys
import keyboardlayout as kl
import keyboardlayout.pygame as klp

class emailPicture:

    def __init__(self):
        key_size = 60
        grey = pygame.Color('grey')
        dark_grey = ~pygame.Color('grey')
        key_info = kl.KeyInfo(
            margin=10,
            color=grey,
            txt_color=dark_grey,
            txt_font=pygame.font.Font('fonts/segoe-ui.ttf', 12),
            txt_padding=(key_size//6, key_size//10)
        )
        keyboard_info = kl.KeyboardInfo(
            position=(0, 1404),
            padding=2,
            color=~grey
        )

        letter_key_size = (key_size, key_size)  # width, height
        keyboard_layout = klp.KeyboardLayout(
            kl.LayoutName.QWERTY,
            keyboard_info,
            letter_key_size,
            key_info
        )

        self.keyboard_layout = keyboard_layout

    def run(self, display = None, events = None):
        top = pygame.image.load("images/top.png").convert()
        bottom = pygame.image.load("images/bottom.png").convert()
        display.fill((255, 255, 255))

        display.blit(top, (0, 0))
        display.blit(bottom, (0, 1704))

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        self.keyboard_layout.draw(display)
        pygame.display.update()

    def __str__(self):
        return "Email step"
