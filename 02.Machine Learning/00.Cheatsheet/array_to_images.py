import pandas as pd
import numpy as np
from PIL import Image
import math

df_test = pd.read_csv(r'02.Chapter\00.Cheatsheet\fashion-mnist_test.csv')
print(df_test.shape)
image_label = df_test.values[0][0]
img_ex = df_test.values[0][1:]
# print(math.sqrt(img_ex.shape[0])) ---- This value will be used in reshape.
img_ex = img_ex.reshape((28,28))
print(img_ex.shape)


img = Image.fromarray(img_ex.astype(int))
img.show()