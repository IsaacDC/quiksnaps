import pygame
import cv2
import numpy as np

pygame.init()

img = cv2.imread('img_3.png')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Converts image to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10, minSize=(140, 140))

# If only one face is detected, it crops around the face
if len(faces) == 1:
    for (x, y, w, h) in faces:
        top_ratio = 0.5
        new_width = 4 * w
        new_height = 5 * h
        new_height_top = int(top_ratio * new_height)
        new_x = max(0, x - (new_width - w) // 2)
        new_y = max(0, y - (new_height_top - h) // 2)
        img = img[new_y:new_y + new_height, new_x:new_x + new_width]

# If more than 1 face is detected it puts a green box around the faces (Testing Purposes)
elif len(faces) > 1:
    x_values, y_values, w_values, h_values = zip(*faces)
    x_min = min(x_values)
    y_min = min(y_values)
    x_max = max(x_values + w_values)
    y_max = max(y_values + h_values)

    # Calculate padding around the bounding box
    padding = 300
    x_min_pad = max(0, x_min - padding)
    y_min_pad = max(0, y_min - padding)
    x_max_pad = min(img.shape[1], x_max + padding)
    y_max_pad = min(img.shape[0], y_max + padding)

    # Crop the image using the padded bounding box
    img = img[y_min_pad:y_max_pad, x_min_pad:x_max_pad]
else:
    print("No faces detected.")

# Set window width and height to the size of the cropped or default image
width, height = img.shape[1], img.shape[0]
window = pygame.display.set_mode((width, height))

# Turns the cv image into a pygame image
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.flip(img, 1)
img = np.rot90(img)
img = pygame.surfarray.make_surface(img)

# Runs pygame
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
