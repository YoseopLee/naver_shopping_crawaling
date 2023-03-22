from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# chromedriver auto update
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip


# Defending chrome off
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# unrequired error message
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# move to wanted website
driver.implicitly_wait(5)
driver.maximize_window() # Screen max
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

# Find Id input
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("dldytjq723")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# Find PW input
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("@dldytjq724")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# Find login button
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()
