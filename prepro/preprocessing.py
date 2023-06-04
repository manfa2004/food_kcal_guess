import os
from PIL import Image
from numpy import expand_dims
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt

korean_foods = {"kalguksu":"칼국수", "champon":"짬뽕", "kimbap":"김밥", "bibimbap":"비빔밥", "bossam":"보쌈",
                "kimchi":"배추김치", "radish kimchi":"깍두기", "dak galbi":"닭갈비", "kimchi fried rice":"김치볶음밥", "bulgogi":"불고기"}
japanese_foods = {"nabe":"鍋", "soba":"そば", "ramen":"ラーメン", "japanese curry":"カレー","sushi":"寿司",
                  "udon":"うどん", "karaage":"唐揚げ","onigiri":"おにぎり","gyudon":"牛丼", "okonomiyaki":"お好み焼き"}
chinese_foods = {"congee":"粥", "dong po rou":"东坡肉", "baozi":"包子", "chaofan":"炒饭", "zhajiangmian":"炸酱面",
                  "sweet and sour pork":"糖醋肉", "mapotofu":"麻婆豆腐", "wonton soup":"馄饨汤", "mooncake":"月饼", "pecking duck":"烤鸭"}

# 이미지 크기 통일
for i, j in korean_foods.items():
    image_name = i.replace(" ", "_")
    file_path = "./" + image_name + '/'
    file_names = os.listdir(file_path)

    for f in file_names:
        img = Image.open(file_path + f)
        resized_img = img.resize((256, 256))

        
        if not os.path.exists("./" + image_name + "_resized"): 
            os.makedirs("./" + image_name + "_resized")

        # <음식이름>_resized 디렉토리에 크기 조정된 이미지 저장
        title, ext = os.path.splitext(f)
        resized_img.save("./" + image_name + "_resized/" + title + "_r" + ext)

# preprocessing
for i, j in korean_foods.items():
    image_name = i.replace(" ", "_")
    file_path = "./" + image_name + "_resized" + '/'
    file_names = os.listdir(file_path)
    print(file_names)
    for f in file_names:
        img = load_img(file_path + f)
        data = img_to_array(img)
        samples = expand_dims(data, 0)
        datagen = ImageDataGenerator(
                                    # rescale=1./255,
                                    zoom_range=[0.8, 1.0],
                                    rotation_range=45,
                                    brightness_range=[0.3, 1.2],
                                    shear_range=0.2,
                                    horizontal_flip=True,
                                    vertical_flip=True,
                                    height_shift_range=0.3,
                                    width_shift_range=0.3
        )
    # ImageDataGenerator로 변경된 이미지 확인
    it = datagen.flow(samples, batch_size=1)
    fig = plt.figure(figsize=(20,20))
    plt.title(i)
    for i in range(12):
        plt.subplot(4, 3, 1 + i)
        batch = it.next()
        image = batch[0].astype('uint8')
        plt.imshow(image)
    plt.show()