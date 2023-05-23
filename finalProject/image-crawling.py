from urllib.parse import quote_plus           
from bs4 import BeautifulSoup as bs  
import time
from urllib.request import (urlopen, urlparse, urlunparse, urlretrieve)
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import os
import pandas as pd


chrome_path ='C:\Temp\chromedriver.exe'
base_url = "https://www.google.co.kr/imghp"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("lang=ko_KR")
chrome_options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(chrome_path,chrome_options=chrome_options)
driver.get(base_url)
driver.implicitly_wait(3) # 로드될 때까지 시간만큼 대기
driver.get_screenshot_as_file('google_screen.png')
driver.close()

def selenium_scroll_option():
  SCROLL_PAUSE_SEC = 3
  
  # 스크롤 높이 가져오기
  last_height = driver.execute_script("return document.body.scrollHeight")
  
  while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져오기
    new_height = driver.execute_script("return document.body.scrollHeight")
  
    if new_height == last_height:
        break
    last_height = new_height


japanese_foods = {"nabe":"鍋", "soba":"そば", "ramen":"ラーメン", "japanese_curry":"カレー","sushi":"寿司",
                  "udon":"うどん", "karaage":"唐揚げ","onigiri":"おにぎり","gyudon":"牛丼", "okonomiyaki":"お好み焼き"}
# chinese_foods = {"congee":"粥", "dong_po_rou":"东坡肉", "baozi":"包子", "chaofan":"炒饭", "zhajiangmian":"炸酱面",
#                  "sweet_and_sour_pork":"糖醋肉", "mapotofu":"麻婆豆腐", "wonton_soup":"馄饨汤", "mooncake":"月饼", "pecking_duck":"烤鸭"}


#for i, j in japanese_foods.items():
for i, j in chinese_foods.items():
    image_name = i.replace(" ", "_")
    seach_word = j

    if not os.path.exists("./" + image_name):
        os.makedirs("./" + image_name)

    driver = webdriver.Chrome(chrome_path)
    driver.get('http://www.google.co.kr/imghp?hl=ko')
    browser = driver.find_element(By.NAME,"q")
    browser.send_keys(seach_word)
    browser.send_keys(Keys.RETURN)

    selenium_scroll_option() # 스크롤

    # 이미지 src요소를 리스트업 -> 이미지 url 저장
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd") 
    images_url = []
    for i in images: 
        if i.get_attribute('src')!= None :
                images_url.append(i.get_attribute('src'))
        else :
            images_url.append(i.get_attribute('data-src'))

    # 겹치는 이미지 url 제거
    print("전체 다운로드한 이미지 개수: {}\n동일한 이미지를 제거한 이미지 개수: {}".format(len(images_url), len(pd.DataFrame(images_url)[0].unique())))
    images_url=pd.DataFrame(images_url)[0].unique()
       
    # 이미지 다운로드
    for t, url in enumerate(images_url, 0):        
        urlretrieve(url, './' + image_name + '/' + image_name + '_' + str(t) + '.jpg')
    driver.close()