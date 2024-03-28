import pygame
import cv2
import numpy as np

pygame.init()

img = cv2.imread('isaac.jpg')

width, height, channels = img.shape
window = pygame.display.set_mode((height, width))

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bodies, _ = hog.detectMultiScale(gray, winStride=(8, 8), padding=(32, 32), scale=1.05)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = np.rot90(img)
img = pygame.surfarray.make_surface(img)
window.blit(img, (0, 0))

for (x, y, w, h) in bodies:
    pygame.draw.rect(window, (0, 255, 0), (x, y, w, h), 2)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.update()

pygame.quit()
