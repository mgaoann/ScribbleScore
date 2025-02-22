#! /opt/homebrew/bin/python3 

import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = input("Enter the image file path: ")   #take user input for file
correct_image = cv2.imread(image_path)
if correct_image is None:
    print("Error: The provided file is not a valid image or does not exist.")
    exit()
else:
    print("Image loaded successfully!")

def pass_filter(img, filter1):
    new_image = np.zeros(np.shape(img), dtype=np.int64) # create new black image

    # Assumes a square filter, eg: 3 x 3, 4 x 4, NOT 3 x 5
    size_offset = int(len(filter1)/2)
                                                                    # Loop for every...
    for y in range(size_offset, img.shape[0] - size_offset):        # row
        for x in range(size_offset, img.shape[1] - size_offset):    # pixel in row
            for c in range(img.shape[2]):                           # color in pixel

                channel_subset = img[y-size_offset : y+size_offset+1, x-size_offset : x+size_offset+1, c]
                new_image[y][x][c] = int(np.sum(np.multiply(filter1, channel_subset)))
    return new_image

def normal(img):    #normalize image, make it good to look at
    minval = np.min(img)
    maxval = np.max(img - minval)
    if (maxval != 0):
        img = ((img - minval) / maxval)
    return img

sobel_y = np.array([[  1,  2,  1],\
                    [  0,  0,  0],\
                    [ -1, -2, -1]])

sobel_x = np.array([[  -1,  0, 1],\
                    [  -2,  0, 2],\
                    [  -1,  0, 1]])

ximg = pass_filter(correct_image, sobel_y)
yimg = pass_filter(correct_image, sobel_x)
outimg = np.sqrt(ximg*ximg + yimg*yimg)

# Create a figure with 1 row and 3 columns
plt.figure(figsize=(12, 4))

# First subplot - Sobel Y
plt.subplot(1, 3, 1)
plt.title("Sobel X")
plt.imshow(normal(ximg), cmap="gray")
plt.axis("off")

# Second subplot - Sobel X
plt.subplot(1, 3, 2)
plt.title("Sobel Y")
plt.imshow(normal(yimg), cmap="gray")
plt.axis("off")

# Third subplot - Combined Edge Detection
plt.subplot(1, 3, 3)
plt.title("Sobel Edge Detection")
plt.imshow(normal(outimg), cmap="gray")
plt.axis("off")

# Show all subplots
plt.tight_layout()
plt.show()
