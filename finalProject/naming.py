import os

japanese_foods = {"nabe":"鍋", "soba":"そば", "ramen":"ラーメン", "japanese_curry":"カレー","sushi":"寿司",
                  "udon":"うどん", "karaage":"唐揚げ","onigiri":"おにぎり","gyudon":"牛丼", "okonomiyaki":"お好み焼き"}
chinese_foods = {"congee":"粥", "dong_po_rou":"东坡肉", "baozi":"包子", "chaofan":"炒饭", "zhajiangmian":"炸酱面",
                  "sweet_and_sour_pork":"糖醋肉", "mapotofu":"麻婆豆腐", "wonton_soup":"馄饨汤", "mooncake":"月饼", "pecking_duck":"烤鸭"}


#for i in japanese_foods.keys():
for i in chinese_foods.keys():
    image_name = i.replace(" ", "_")
    file_path = "./" + image_name + '/'
    file_names = os.listdir(file_path)

    j = 0
    for name in file_names:
        src = file_path + name
        dst = os.path.join(file_path, i + '_' + str(j) + '.jpg')
        os.rename(src, dst)
        j+=1