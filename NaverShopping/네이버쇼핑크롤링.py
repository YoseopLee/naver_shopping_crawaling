from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# chromedriver 자동업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import csv

# 크롬 자동꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 필요없는 에러메세지 스킵
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 원하는 검색어페이지로 이동
query = input("네이버쇼핑 검색어를 입력하세요 : ")
url = "https://search.shopping.naver.com/search/all?frm=NVSHCHK&origQuery=" + query + "&pagingIndex=1&pagingSize=40&productSet=checkout&query=" + query + "&sort=rel&timestamp=&viewType=list"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window() # Screen max
driver.implicitly_wait(5) #로딩이 끝날 때까지 5초까지는 기다려줌

driver.get(url)

# 네이버페이 on
driver.find_element(By.CLASS_NAME, "subFilter_btn_align__LfEXs").click()

# 스크롤 전 높이
before_h = driver.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

    # 스크롤 사이에 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

#파일 생성 (경로, 방식, 인코딩, 줄바꿈 방지)
f = open(r"C:\Users\Admin\OneDrive\바탕 화면\naver_crawling\NaverShopping\data.csv", 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)

# 상품 정보 div
items = driver.find_elements(By.CLASS_NAME, "basicList_info_area__TWvzp")

for item in items:
    link = item.find_element(By.CLASS_NAME, "basicList_title__VfX3c > a")
    
    # link 페이지 열기
    link.send_keys(Keys.CONTROL + "\n")
    driver.switch_to.window(driver.window_handles[1])

    # 스마트스토어 아닐 시 예외처리
    try:
        name = driver.find_element(By.CLASS_NAME, "_22kNQuEXmb").text
        tags = driver.find_elements(By.CLASS_NAME, "_2RkVi-H2ze")
        print(name)
        product_info = [name]
        for tag in tags:
            tag_name = tag.find_element(By.CLASS_NAME, "_3SMi-TrYq2").text
            print(tag_name)
            product_info.append(tag_name)
        
    except:
        product_info = "자사몰입니다."

    csvWriter.writerow(product_info)    
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
f.close()