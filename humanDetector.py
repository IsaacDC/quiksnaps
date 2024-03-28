import pygame
import cv2
import numpy as np

pygame.init()

img = cv2.imread('IsaacTest.jpg')

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# upper_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bodies, _ = hog.detectMultiScale(gray, winStride=(8, 8), padding=(32, 32), scale=1.1)

sorted_bodies = sorted(bodies, key=lambda x: x[2] * x[3], reverse=True)

if len(sorted_bodies) > 0:
    (x, y, w, h) = sorted_bodies[0]
    cropped_img = img[y:y+h, x:x+w]
else:
    print("No upper bodies detected.")
    pygame.quit()
    exit()

width, height = w, h
window = pygame.display.set_mode((width, height))

cropped_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
cropped_img = np.rot90(cropped_img)
cropped_img = pygame.surfarray.make_surface(cropped_img)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            running = False

    window.blit(cropped_img, (0, 0))
    pygame.display.update()

pygame.quit()
