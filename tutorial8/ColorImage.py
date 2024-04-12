import cv2
import matplotlib.pyplot as plt

# Load the color image
image = cv2.imread('tutorial8/avatar.jpg')

# Convert BGR to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Convert BGR to LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Display all versions
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(rgb_image)
plt.title('RGB Image')

plt.subplot(2, 2, 2)
plt.imshow(hsv_image)
plt.title('HSV Image')

plt.subplot(2, 2, 3)
plt.imshow(lab_image)
plt.title('LAB Image')

plt.show()