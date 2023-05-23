import os
import json

japanese_foods = {"nabe":"鍋", "soba":"そば", "ramen":"ラーメン", "japanese_curry":"カレー","sushi":"寿司",
                  "udon":"うどん", "karaage":"唐揚げ","onigiri":"おにぎり","gyudon":"牛丼", "okonomiyaki":"お好み焼き"}
chinese_foods = {"congee":"粥", "dong_po_rou":"东坡肉", "baozi":"包子", "chaofan":"炒饭", "zhajiangmian":"炸酱面",
                  "sweet_and_sour_pork":"糖醋肉", "mapotofu":"麻婆豆腐", "wonton_soup":"馄饨汤", "mooncake":"月饼", "pecking_duck":"烤鸭"}

#for i in chinese_foods.keys():
for i in japanese_foods.keys():
    image_name = i.replace(" ", "_")
    file_names = os.listdir('./'+image_name)

    tmp_json = []
   
    for j in file_names:
        tmp_json.append(
        {
        'image_id': j,
        'label': image_name
        }
        )
    
    with open(i + '.json', 'w') as outfile:
        json.dump(tmp_json, outfile, indent=4, sort_keys=True)