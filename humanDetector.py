import pygame
import cv2
import numpy as np

pygame.init()

img = cv2.imread('img.png')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

sorted_faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)

if len(sorted_faces) == 1:
    (x, y, w, h) = sorted_faces[0]
    top_ratio = 0.5
    new_width = 4 * w
    new_height = 5 * h
    new_height_top = int(top_ratio * new_height)
    new_x = max(0, x - (new_width - w) // 2)
    new_y = max(0, y - (new_height_top - h) // 2)
    img = img[new_y:new_y + new_height, new_x:new_x + new_width]

elif len(sorted_faces) > 1:
    for (x,y,w,h) in sorted_faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

else:
    print("No faces detected. Trying eye detection...")

    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

    if len(eyes) >= 2:
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
    else:
        print("No faces or eyes detected.")
        pygame.quit()
        exit()
    pygame.quit()
    exit()

width, height = img.shape[1], img.shape[0]
window = pygame.display.set_mode((width, height))

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.flip(img, 1)
img = np.rot90(img)
img = pygame.surfarray.make_surface(img)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            running = False

    window.blit(img, (0, 0))
    pygame.display.update()

pygame.quit()
