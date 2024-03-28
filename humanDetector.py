import pygame
import cv2
import numpy as np

# Initialize Pygame
pygame.init()

# Set up Pygame display
width, height = 640, 480
window = pygame.display.set_mode((width, height))

# Initialize the webcam (you may need to adjust the index based on your system)
cap = cv2.VideoCapture(0)

# Load the pre-trained face detection model

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit loop on window close
            break

    # Read the webcam feed
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    pedestrians, _ = hog.detectMultiScale(gray, winStride=(8, 8), padding=(32, 32), scale=1.05)

    for (x, y, w, h) in pedestrians:
        pygame.draw.rect(window, (0, 255, 0), (x, y, w, h), 2)

    pygame.display.update()

    # Convert the OpenCV frame to Pygame format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    window.blit(frame, (0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

# Release the webcam and close Pygame
cap.release()
pygame.quit()
