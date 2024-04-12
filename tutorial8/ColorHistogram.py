import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('tutorial8/avatar.jpg')

# Split the image into its RGB channels
r_channel, g_channel, b_channel = cv2.split(image)

# Calculate histograms for each channel
r_hist = cv2.calcHist([r_channel], [0], None, [256], [0, 256])
g_hist = cv2.calcHist([g_channel], [0], None, [256], [0, 256])
b_hist = cv2.calcHist([b_channel], [0], None, [256], [0, 256])

# Plot histograms
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(r_hist, color='red')
plt.title('Red Channel Histogram')

plt.subplot(3, 1, 2)
plt.plot(g_hist, color='green')
plt.title('Green Channel Histogram')

plt.subplot(3, 1, 3)
plt.plot(b_hist, color='blue')
plt.title('Blue Channel Histogram')

plt.tight_layout()
plt.show()
