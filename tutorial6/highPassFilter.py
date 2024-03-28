import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('./tutorial6/avatar.jpg', 0)  # Load image in grayscale

# Step 2: Perform Fourier Transform
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)

# Step 3: Create a high-pass filter
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2
mask = np.ones((rows, cols), np.uint8)
r = 30  # Radius of the high-pass filter
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 0

# Step 4: Apply the filter
f_transform_shifted_filtered = f_transform_shifted * mask

# Step 5: Inverse Fourier Transform
f_transform_filtered = np.fft.ifftshift(f_transform_shifted_filtered)
image_filtered = np.fft.ifft2(f_transform_filtered)
image_filtered = np.abs(image_filtered)

# Step 6: Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(np.log(1 + np.abs(f_transform_shifted)), cmap='gray')
plt.title('Fourier Transformed Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(image_filtered, cmap='gray')
plt.title('High-Pass Filtered Image')
plt.axis('off')

plt.show()
