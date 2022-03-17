from PIL import Image
import numpy as np
import os

img = Image.open(r"02.Chapter\00.Cheatsheet\test_image2.jpg")


# Getting the image parameters such as shape, pixels
# print(img)
# print(img.size)
# arr = np.array(img, dtype=float)
# print(arr.shape)
# img.show()

# Converting image to RGBA & L
# img = img.convert("L") # RGBA-Transperency, RGB-color, L-Greyscale
# img.show()
# arr = np.array(img, dtype=float)
# print(arr.shape)

# Resizing the image
img = img.resize((200,200))
img.show()
arr = np.array(img, dtype=float)
print(arr)