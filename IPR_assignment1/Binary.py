import cv2
import matplotlib.pyplot as plt

def make_photo_binary(input_threshold, filepath):
    img_path = filepath
    original_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    grayscale_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(grayscale_img, input_threshold, 255, cv2.THRESH_BINARY)
    rows = 1
    column = 2
    figure = plt.figure(figsize=(20, 10))

    figure.add_subplot(rows, column, 1)
    plt.imshow(original_img_rgb)
    plt.title("Original Image")
    figure.add_subplot(rows, column, 2)

    plt.imshow(binary_img, cmap="gray") 
    plt.title("Binary Image with Threshold = " + str(input_threshold))
    plt.tight_layout() 
    plt.show()  