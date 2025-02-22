#! /opt/homebrew/bin/python3 

import cv2
import matplotlib.pyplot as plt
import numpy as np

# image_path = input("Enter the image file path: ")   #take user input for file
# correct_image = cv2.imread(image_path)
# if correct_image is None:
#     print("Error: The provided file is not a valid image or does not exist.")
#     exit()
# else:
#     print("Image loaded successfully!")

def pass_filter(img, filter1):
    new_image = np.zeros(np.shape(img), dtype=np.int64) # create new black image

    # Assumes a square filter, eg: 3 x 3, 4 x 4, NOT 3 x 5
    size_offset = int(len(filter1)/2)
                                                                    # Loop for every...
    for y in range(size_offset, img.shape[0] - size_offset):        # row
        for x in range(size_offset, img.shape[1] - size_offset):    # pixel in row
            #for c in range(img.shape[2]):                           # color in pixel

                channel_subset = img[y-size_offset : y+size_offset+1, x-size_offset : x+size_offset+1]
                new_image[y][x] = int(np.sum(np.multiply(filter1, channel_subset)))
    return new_image

def normal(img):    #normalize image, make it good to look at
    minval = np.min(img)
    maxval = np.max(img - minval)
    if (maxval != 0):
        img = ((img - minval) / maxval)
    return img
def curve(img):        #increase contrast, gets rid of noise
    for y in range(img.shape[0]):        # row
        for x in range(img.shape[1]):    # pixel in row
            if(img[y][x] < 64):
                img[y][x] = 0
            elif (img[y][x] > 192):
                img[y][x] = 255
            else:
                img[y][x] = min(img[y][x] * 2 - 128, 255)
    return img/255
def sobel(img):
    sobel_y = np.array([[  1,  2,  1],\
                        [  0,  0,  0],\
                        [ -1, -2, -1]])

    sobel_x = np.array([[  -1,  0, 1],\
                        [  -2,  0, 2],\
                        [  -1,  0, 1]])

    ximg = pass_filter(img, sobel_y)
    yimg = pass_filter(img, sobel_x)
    outimg = np.sqrt(ximg*ximg + yimg*yimg)
    return outimg
