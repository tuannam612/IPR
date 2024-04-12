import cv2
import numpy as np

# Load the color image
image = cv2.imread('tutorial8/avatar.jpg')

# Adjust brightness and contrast
alpha = 1.5  # Contrast control (1.0-3.0)
beta = 30    # Brightness control (0-100)
bright_contr_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Modify saturation and hue in HSV space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Modify saturation
saturation_factor = 1.5  # Increase saturation by a factor of 1.5
hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_factor, 0, 255)

# Modify hue
hue_shift = 20  # Shift hue by 20 degrees (0-360)
hsv_image[:, :, 0] = (hsv_image[:, :, 0] + hue_shift) % 180

# Convert HSV back to BGR
hue_sat_modified_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Display the original and modified images
cv2.imshow('Original Image', image)
cv2.imshow('Brightness and Contrast Adjusted Image', bright_contr_image)
cv2.imshow('Hue and Saturation Modified Image', hue_sat_modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
