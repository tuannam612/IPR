import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('tutorial8/BenTheChunkyCat.jpg')

# Convert image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the green color
lower_green = np.array([35, 50, 50])  # Lower bound for green in HSV
upper_green = np.array([85, 255, 255])  # Upper bound for green in HSV

# Create a mask to isolate the green color
mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Apply the mask to the original image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display the original image, mask, and segmented image
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title('Mask')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.title('Segmented Image')

plt.show()
