from tkinter import image_names
from matplotlib import image
from matplotlib import pyplot
import pandas as pd
import statsmodels.api as sm
import numpy as np

def on_all(image_array, func):
    for img in image_array:
        func(img)

def print_img(img):
    print(img)
    print()

def show_img(img):
    pyplot.imshow(img)
    pyplot.show()

def sumsum(image):
    return sum(sum(image))

def simplify(image):
    for i in range(0, 10):
        for j in range(0, 8):
            if(image[i][j] == 255):
                image[i][j] = 0
            else:
                image[i][j] = 1

image_x = image.imread("C:/Users/edmun/x.jpg")
image_y = image.imread("C:/Users/edmun/y.jpg")
image_unknown = image.imread("C:/Users/edmun/unknown.jpg")

image_array = [image_x, image_y, image_unknown]

import imageio

bitmap_x = imageio.imread("C:/Users/edmun/x.bmp")
bitmap_y = imageio.imread("C:/Users/edmun/y.bmp")
bitmap_unknown = imageio.imread("C:/Users/edmun/unknown.bmp")

bitmap_array = [bitmap_x, bitmap_y, bitmap_unknown]

on_all(bitmap_array, simplify)
#on_all(bitmap_array, print_img)

bit_x_flat = bitmap_array[0].flatten()
bit_y_flat = bitmap_array[1].flatten()
bit_un_flat = bitmap_array[2].flatten()

print("X")
print(bit_x_flat)

A=[0,0,0,0,0,0,0,0,
   0,0,0,1,1,0,0,0,
   0,0,1,1,1,1,0,0,
   0,0,1,0,0,1,0,0,
   0,0,1,0,0,1,0,0,
   0,0,1,1,1,1,0,0,
   0,0,1,0,0,1,0,0,
   0,1,1,0,0,1,1,0,
   0,1,0,0,0,0,1,0,
   0,0,0,0,0,0,0,0]

#print(bit_x_flat)

X = np.transpose(pd.DataFrame(zip(bit_x_flat, bit_y_flat, A), columns = ['X', 'Y', 'A']))
Y = np.array([1, 0, 2])


X = sm.add_constant(X)
 
model = sm.OLS(Y, X)
result = model.fit()

print(result.summary())
print(result.predict(bit_un_flat))