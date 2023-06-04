# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import utils
# from tensorflow.keras import layers
# from tensorflow.keras import datasets
# from tensorflow.keras.callbacks import EarlyStopping
# from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

from pathlib import Path
import pandas as pd
import json

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


os.chdir("c:/Users/user/Desktop/food_kcal_guess/Dataset")

a = os.listdir()

for i in a:
    link = "c:/Users/user/Desktop/food_kcal_guess/Dataset/" + i
    os.chdir(link)
    for j in os.listdir():
        if ".json" in j:
            link2 = link + "/" + j
            with open(link2, "r") as f:
                js = json.load(f)
            df = pd.DataFrame(js)
    #         print(df)
    # print(i)


with open("c:/Users/user/Desktop/food_kcal_guess/Dataset/japanese_foods/ramen.json", "r") as f:
    js = json.load(f)
df = pd.DataFrame(js)

# print(df["image_id"][1])
print(df)

plt.figure(figsize=(10,10))

for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    li = "c:/Users/user/Desktop/food_kcal_guess/Dataset/japanese_foods/"+ df["label"][i] + "/" + df["image_id"][i]
    image = mpimg.imread(li)
    plt.imshow(image, cmap=plt.cm.binary)
    plt.xlabel(df["label"][i])

plt.show()
