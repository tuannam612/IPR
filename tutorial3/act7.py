import cv2

# Load an image
image = cv2.imread('BenTheChunkyCat.jpg')

# Convert the image to HSV and YCbCr color spaces
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Display the separate channels of the HSV image
h, s, v = cv2.split(hsv_image)
cv2.imshow('Hue Channel', h)
cv2.imshow('Saturation Channel', s)
cv2.imshow('Value Channel', v)

# Display the separate channels of the YCbCr image
y, cb, cr = cv2.split(ycbcr_image)
cv2.imshow('Y Channel', y)
cv2.imshow('Cb Channel', cb)
cv2.imshow('Cr Channel', cr)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()