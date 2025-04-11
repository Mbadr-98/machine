import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread(r'opencv.png')

# Averaging filter (blur)
averaged = cv2.blur(img, (5, 5))

# Gaussian blur
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Median filter (for noise reduction)
median_blur = cv2.medianBlur(img, 5)

# Display all the results in a grid for comparison
titles = ['Original', 'Averaging', 'Gaussian Blur', 'Median Blur']
images = [img, averaged, gaussian_blur, median_blur]

# Plot each image with its respective title
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display in matplotlib
    plt.title(titles[i])
    plt.axis('off')

plt.show()