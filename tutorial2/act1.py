

import random                   
import cv2                        
import matplotlib.pyplot as plt   
import os                          
from PIL import Image               
import numpy

"""
The function to load an image and convert it to greyscale
"""
def loadGrayScale():
    img_path = r"BenTheChunkyCat.jpg"

    black_and_white_img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)

    return black_and_white_img

"""
The function to display the greyscale image
"""
def displayBlackAndWhite(black_and_white_img):
    plt.imshow(black_and_white_img,cmap='gray')

    plt.title("Greyscale Image")
    plt.show()

"""
The function to set global threshold
"""
def globalThreshold(black_and_white_img):

    thresholdValue = numpy.average([0,255])

    _, binaryImage = cv2.threshold(black_and_white_img, thresholdValue, 255, cv2.THRESH_BINARY)

    return binaryImage

"""
The function to display the binary image
"""
def showImageUsingMathPlot(binaryImage):
    plt.imshow(binaryImage,cmap="grey")

    plt.title("Binary Image")
    plt.show()

"""
Invoking functions
"""

black_and_white_img = loadGrayScale()
displayBlackAndWhite(black_and_white_img)

binaryImageDisplay = globalThreshold(black_and_white_img)
showImageUsingMathPlot(binaryImageDisplay)
