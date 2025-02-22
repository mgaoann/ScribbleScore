#! /opt/homebrew/bin/python3 

import cv2
import matplotlib.pyplot as plt
from sobel import sobel, normal, curve


import numpy as np
import matplotlib.pyplot as plt

# Assume `img` is your 2D grayscale image array (values between 0-255)
# Example: img = np.array([[0, 50], [200, 255]])  # Small 2x2 example

def plot_best_fit(img):
    h = img.shape[0]
    w = img.shape[1]
    # Generate X and Y coordinates
    X, Y = np.meshgrid(np.arange(w), np.arange(h,0,-1))
    X = X.flatten()
    Y = Y.flatten()
    intensities = img.flatten()
    # Compute line of best fit using NumPy's polyfit (degree = 1 for linear)
    m, b = np.polyfit(X, Y, 1, w=intensities)  # y = mx + b

    # Generate the best fit line values
    fit = m * X + b



    plt.figure(figsize=(12, 2))
    plt.subplot(1, 2, 1)
    # Plot scatter points
    plt.scatter(X, Y, c=intensities, cmap='grey', s=intensities, alpha=0.5, label="Pixel Intensities")
    # Plot best-fit line
    plt.plot(X, fit, color='red', linewidth=2, label="Best Fit Line")
    plt.ylim(0, h)
    plt.xlim(0, w)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('xkcd:black')
    # Labels and title
    plt.xlabel("X (width)")
    plt.ylabel("Y (height)")
    plt.title("Line of Best Fit for Grayscale Image")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.title("Sobel Edge Detection")
    plt.imshow(sobelimg, cmap="gray")
    plt.axis("off")

    plt.show()



image_path = input("Enter the image file path: ")   #take user input for file
correct_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if correct_image is None:
    print("Error: The provided file is not a valid image or does not exist.")
    exit()
else:
    print("Image loaded successfully!")

sobelimg = curve(sobel(correct_image))

#plot_best_fit(sobelimg)

# plt.title("Sobel Edge Detection")
# plt.imshow(sobelimg, cmap="gray")
# plt.axis("off")
# plt.tight_layout()
# plt.show()

plot_best_fit(sobelimg)
