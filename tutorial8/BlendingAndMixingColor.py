import cv2
import numpy as np

# Load the color image
image = cv2.imread('tutorial8/avatar.jpg')

# Apply Sepia filter
def apply_sepia(image):
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    sepia_image = cv2.transform(image, sepia_filter)
    return sepia_image

# Create a 'color pop' effect
def color_pop(image, color_to_retain):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Selectively retain a single color (specified by its channel)
    b, g, r = cv2.split(image)
    if color_to_retain == 'blue':
        color_pop_image = cv2.merge((b, np.zeros_like(g), np.zeros_like(r)))
    elif color_to_retain == 'green':
        color_pop_image = cv2.merge((np.zeros_like(b), g, np.zeros_like(r)))
    elif color_to_retain == 'red':
        color_pop_image = cv2.merge((np.zeros_like(b), np.zeros_like(g), r))
    else:
        raise ValueError("Invalid color specified. Choose 'red', 'green', or 'blue'.")
    
    return color_pop_image

# Apply sepia filter
sepia_image = apply_sepia(image)

# Create 'color pop' effect (retain only blue color)
color_pop_image = color_pop(image, 'blue')

# Display the original image, sepia filtered image, and color pop image
cv2.imshow('Original Image', image)
cv2.imshow('Sepia Filtered Image', sepia_image)
cv2.imshow('Color Pop Effect (Blue)', color_pop_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
