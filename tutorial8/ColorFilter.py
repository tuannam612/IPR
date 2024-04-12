import cv2
import numpy as np

# Load the color image
image = cv2.imread('tutorial8/avatar.jpg')

# Apply Sepia filter
sepia_filter = np.array([[0.393, 0.769, 0.189],
                         [0.349, 0.686, 0.168],
                         [0.272, 0.534, 0.131]])
sepia_image = cv2.transform(image, sepia_filter)

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Selectively retain a single color (e.g., blue) in grayscale image
b, g, r = cv2.split(image)
color_pop_image = cv2.merge((b, g, np.zeros_like(r)))

# Display the original, sepia, and color pop images
cv2.imshow('Original Image', image)
cv2.imshow('Sepia Filtered Image', sepia_image)
cv2.imshow('Color Pop Effect', color_pop_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
